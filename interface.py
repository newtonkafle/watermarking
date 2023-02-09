import tkinter as tk
from inner_workings import FirstPageHandlers, MainPageHandlers
from PIL import Image, ImageTk


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Watermark Everything')
        self.geometry('500x300')
        self.frame = FirstPage(self)

    def openpage2(self, image=None):
        self.frame.destroy()
        self.frame = MainPage(self)
        self.frame.load_images(image)


class FirstPage(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        # initializing the handlers
        self.handlers = FirstPageHandlers()

        # creating the image object to import into the canvas
        self.logo = tk.PhotoImage(height=200, width=200, file='../logo.png')

        # creating the canvas for the image
        self.image_canvas = tk.Canvas(self, height=200, width=200)
        self.image_canvas.create_image(100, 100, image=self.logo)
        self.image_canvas.grid(column=0, row=0, padx=30, pady=50)

        # creating the frame for all the buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(column=1, row=0, padx=60)

        # creating the buttons for the frame
        self.btn_open_image = tk.Button(
            self.button_frame, text='Open Image', command=self.open_image)
        self.btn_open_image.grid(column=0, row=0, sticky='w', pady=3)
        self.btn_bulk_water_mark = tk.Button(
            self.button_frame, text='Bulk WaterMark')
        self.btn_bulk_water_mark.grid(column=0, row=1, sticky='w', pady=3)
        self.btn_exit_window = tk.Button(
            self.button_frame, text='Exit', command=self.quit)
        self.btn_exit_window.grid(column=0, row=2, sticky='w', pady=3)

    def open_image(self):
        '''passing the image onject returned by the handle image method to openpage2'''
        self.master.openpage2(self.handlers.handle_image())


class MainPage(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # providing the size to the window
        self.master.geometry('1000x600')

        # initializing the handlers
        self.handlers = MainPageHandlers()

        self.grid()
        self.image = None
        self.load_item_to_interface()
        # creating the buttons on the top of the window
        self.button_frame = tk.Frame(
            self, pady=15)
        self.button_frame.grid(column=1, row=0, columnspan=4)
        self.btn_add_text = tk.Button(
            self.button_frame, text="Add text", command="")
        self.btn_add_text.grid(column=0, row=0, padx=10)
        self.btn_add_logo = tk.Button(self.button_frame, text="Add logo")
        self.btn_add_logo.grid(column=1, row=0)

        # # creating the empty labels
        em1 = tk.Label(self)
        em1.grid(column=0, row=1)

        # creating a canvas
        self.picture_canvas = tk.Canvas(self,
                                        width=700, height=500, background='black')

        self.picture_canvas.grid(column=1, row=1, pady=5, sticky='w')

        # creating frame for the propertise fields
        self.properties_frame = tk.Frame(self)
        self.properties_frame.grid(row=1, column=2, sticky='nw', pady=50)

        labels = ('Font:', 'Font Size:', 'Font Color:', 'Text:')
        for i, item in enumerate(labels):
            label = tk.Label(self.properties_frame, text=item)
            label.grid(row=i+1, column=0, sticky='w')

        # creating the variables to track the values of the option box
        font_choice = tk.StringVar()
        font_size_choice = tk.IntVar()
        font_color_choice = tk.StringVar()

        # creating the combobox to choose the fonts
        self.font_box = tk.OptionMenu(
            self.properties_frame, font_choice, *
            self.handlers.handle_combo_boxes()[0],
            command=self.handlers.get_font_choice)
        self.font_box.grid(row=1, column=2, sticky='w')

        # creating the option  box for font sizes
        self.font_size_box = tk.OptionMenu(
            self.properties_frame, font_size_choice, *
            self.handlers.handle_combo_boxes()[1],
            command=self.handlers.get_font_size_choice)
        self.font_size_box.grid(row=2, column=2, sticky='w')

        # creating the option box choose the colors
        self.font_color_box = tk.OptionMenu(
            self.properties_frame, font_color_choice, *
            self.handlers.handle_combo_boxes()[2],
            command=self.handlers.get_font_color_choice)
        self.font_color_box.grid(row=3, column=2, sticky='w')

        self.update()

    def load_item_to_interface(self):
        # loading the fonts to select
        self._drag_item_details = {'x': 0, 'y': 0, "item": None}

    def load_images(self, image):
        '''pass images to the handlers which return the photo objects for the canvas'''
        self.image = self.handlers.load_images(image=image)
        self.picture_canvas.create_image(
            350, 250, image=self.image)
        self.update()

    # support for the drag and drop


if __name__ == "__main__":
    app = App()
    app.mainloop()
