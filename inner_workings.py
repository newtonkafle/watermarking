
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import font
import matplotlib.colors as clr


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
        self.fonts = list(font.families())
        self.fonts_sizes = [size for size in range(100)]
        self.font_colors = clr.CSS4_COLORS.keys()

        # handling images
        self.image = None

        # record drag items
        self._drag_item_details = {'x': 0, 'y': 0, "item": None}

        # fonts details
        self.font_family = None
        self.font_size = None
        self.font_weight = None

    def get_drag_item_details(self):
        return self._drag_item_details

    def set_drag_item_details(self, item=None, x=None, y=None):
        self._drag_item_details['item'] = item
        self._drag_item_details['x'] = x
        self._drag_item_details['y'] = y

    # combo box hnadlers

    def handle_combo_boxes(self):
        return (self.fonts, self.fonts_sizes, self.font_colors)

    def get_font_choice(self, choice):
        return choice

    def get_font_size_choice(self, choice):
        return choice

    def get_font_color_choice(self, choice):
        return choice

    def load_images(self, image):
        image1 = Image.open(image.filename)
        image1.load()
        image1 = image1.resize((700, 500), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image1)

    # drag and drop support
    def drag(self, event):
        delta_x = event.x - self._drag_item_details['x']
        delta_y = event.y - self._drag_item_details['y']

        # record the new position
        self._drag_item_details['x'] = event.x
        self._drag_item_details['y'] = event.y

        return delta_x, delta_y

    def drag_stop(self):
        self._drag_item_details['items'] = None
        self._drag_item_details['x'] = 0
        self._drag_item_details['y'] = 0

    # getting the current font details

    def get_current_font_details(self, curr_font):
        font_obj = font.nametofont(curr_font)
        font_obj = font_obj.actual()
        self.font_family = font_obj['family']
        self.font_size = font_obj['size']
        self.font_weight = font_obj['weight']
        print(font_obj)
