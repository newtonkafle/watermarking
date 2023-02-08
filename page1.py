import tkinter as tk
from tkinter import filedialog
from PIL import Image


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Watermark Everything')
        self.geometry('500x300')
        self.frame = FirstPage(self)

    def openpage2(self, image=None):
        self.frame.destroy()
        self.frame = EditPage(self)
        self.frame.load_image(image)


class FirstPage(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        # creating the image object to import into the canvas
        self.logo = tk.PhotoImage(height=200, width=200, file='./logo.png')

        # creating the canvas for the image
        self.image_canvas = tk.Canvas(self, height=200, width=200)
        self.image_canvas.create_image(100, 100, image=self.logo)
        self.image_canvas.grid(column=0, row=0, padx=30, pady=50)

        # creating the frame for all the buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(column=1, row=0, padx=60)
        self.btn_open_image = tk.Button(
            self.button_frame, text='Open Image', command=self.handle_image)
        self.btn_open_image.grid(column=0, row=0, sticky='w', pady=3)
        self.btn_bulk_water_mark = tk.Button(
            self.button_frame, text='Bulk WaterMark')
        self.btn_bulk_water_mark.grid(column=0, row=1, sticky='w', pady=3)
        self.btn_exit_window = tk.Button(
            self.button_frame, text='Exit', command=self.quit)
        self.btn_exit_window.grid(column=0, row=2, sticky='w', pady=3)

    def handle_image(self):
        '''ask user for the image and initialized path to the image'''
        self.image_file = filedialog.askopenfilename(
            initialdir='/', title='select file')
        im = Image.open(self.image_file)
        if im is not None:
            self.master.openpage2(im)


class EditPage(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.geometry('800x600')
        self.update()
        self.window_width = self.master.winfo_width()
        self.grid()
        self.button_frame = tk.Frame(
            self, padx=(self.window_width/2 - 80), pady=15)
        self.button_frame.grid(column=1, row=0, columnspan=3)
        self.btn_add_text = tk.Button(self.button_frame, text="Add text")
        self.btn_add_text.grid(column=0, row=0, padx=10)
        self.btn_add_logo = tk.Button(self.button_frame, text="Add logo")
        self.btn_add_logo.grid(column=1, row=0)

        # creating the empty labels
        em1 = tk.Label(self)
        em2 = tk.Label(self)
        em1.grid(column=0, row=1)
        em2.grid(column=2, row=1)

        # creating a canvas
        self.picture_canvas = tk.Canvas(self,
                                        width=700, height=500, background='green')
        self.picture_canvas.grid(column=1, row=1, padx=25, pady=5)

        self.master.bind('<Configure>', self.get_window_size)

    def get_window_size(self, event):
        # adding the responsive design for the buttons
        if event.widget == self.master:
            self.button_frame.configure(padx=event.width/2 - 100)
            print(self.window_width)

    # initilaized the image to load
    def load_image(self, image):
        print(image.filename)
        # self.image = tk.PhotoImage(
        #     width=image.size[0], height=image.size[1], file=f'{image.filename}')


app = App()
app.mainloop()
