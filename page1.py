import tkinter as tk
from tkinter import filedialog


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Watermark Everything')
        self.geometry('500x300')
        self.frame = FirstPage(self)

    def openpage2(self):
        self.frame.destroy()
        self.frame = Page2(self)


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
        self.filename = filedialog.askopenfilename(
            initialdir='/', title='select file')
        print(self.filename)


class Page2(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.geometry('400x400')
        self.grid()
        self.welcome = tk.Label(self, text='welcome to the application ')
        self.welcome.grid()


app = App()
app.mainloop()
