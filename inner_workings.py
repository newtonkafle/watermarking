
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

    # combo box hnadlers
    def handle_combo_boxes(self):
        return (self.fonts, self.fonts_sizes, self.font_colors)

    def get_font_choice(self, choice):
        print(choice)

    def get_font_size_choice(self, choice):
        print(choice)

    def get_font_color_choice(self, choice):
        print(choice)

    def load_images(self, image):
        image1 = Image.open(image.filename)
        image1.load()
        image1 = image1.resize((700, 500), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image1)
