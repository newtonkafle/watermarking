
from PIL import Image, ImageTk, ImageFont, ImageDraw
from tkinter import filedialog
from tkinter import font
import matplotlib.colors as clr
import glob
import os


F_PATH = '/Users/newtonkafle/Library/Fonts'


class FirstPageHandlers:
    def __init__(self) -> None:
        self.image_file = None
        self.image = None

    def handle_image(self):
        self.image_file = filedialog.askopenfilename(
            initialdir='/', title='select file')

        self.image = Image.open(self.image_file)
        if self.image is not None:
            return self.image


class MainPageHandlers:
    def __init__(self):

        # details for loading up the fonts
        self._fonts = []
        self._fonts_sizes = []
        self._font_colors = []

        self.load_fonts()

        # handling images
        self.image = None
        self.thumbnail_image = None

        # record drag items
        self._drag_item_details = {'x': 0, 'y': 0, "item": None}

        # image co-ordinates
        self.image_x = 0
        self.image_y = 0

        # record the text to be watermarked
        self.water_mark_text = 'Your text Here'

        # fonts details
        self.font_family = None
        self.font_size = None
        self.font_weight = None
        self.font_color = None

    def load_fonts(self):
        fonts = glob.glob(pathname=f'{F_PATH}'+"/*.ttf")
        for font in fonts:
            font = os.path.basename(font)[:-4]
            self._fonts.append(font)
        self._fonts_sizes = [size for size in range(100)]
        self._font_colors = clr.CSS4_COLORS.keys()

    def get_drag_item_details(self):
        return self._drag_item_details

    def set_drag_item_details(self, item=None, x=None, y=None):
        self._drag_item_details['item'] = item
        self._drag_item_details['x'] = x
        self._drag_item_details['y'] = y

    # combo box hnadlers

    def handle_combo_boxes(self):
        return (self._fonts, self._fonts_sizes, self._font_colors)

    def load_images(self, image):
        self.image = Image.open(image.filename)
        self.image.load()
        self.thumbnail_image = self.image.resize((700, 500), Image.ANTIALIAS)
        return ImageTk.PhotoImage(self.thumbnail_image)

    # drag and drop support
    def drag(self, event):
        distace_of_x = event.x - self._drag_item_details['x']
        distance_of_y = event.y - self._drag_item_details['y']

        # record the co-ordinates of the  new position
        self._drag_item_details['x'] = event.x
        self._drag_item_details['y'] = event.y

        return distace_of_x, distance_of_y

    def drag_stop(self):
        self._drag_item_details['items'] = None
        self._drag_item_details['x'] = 0
        self._drag_item_details['y'] = 0

    # getting the current font details
    def get_current_font_details(self, curr_font):
        font_obj = font.nametofont(curr_font)
        font_obj = font_obj.actual()
        self.font_family = font_obj['family'][1:]
        self.font_size = font_obj['size']
        self.font_weight = font_obj['weight']

    def write_on_image(self):

        edit_image = ImageDraw.Draw(self.image)
        font = f'{F_PATH}/{self.font_family}.ttf'
        img_font = ImageFont.truetype(
            font=font, size=self.font_size)

        # getting the original image size
        (width, height) = self.image.size

        # getting the text size
        (text_w, text_h) = edit_image.textsize(self.water_mark_text)

        # upscaling the image here
        self.image_y = self.image_y * (height/500)
        if self.image_x > 1690:
            self.image_x = self.image_x + text_w
        elif self.image_x > 125:
            self.image_x = self.image_x * (width/700) - text_w
        else:
            self.image_x = self.image_x - text_w/2

        edit_image.text(
            (self.image_x, self.image_y),
            text=self.water_mark_text,
            fill=self.font_color,
            font=img_font,
        )
        self.image.save('result.jpg')
