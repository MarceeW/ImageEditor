import tkinter.filedialog
from tkinter import *

import customtkinter
from PIL import Image, ImageTk, ImageFilter


class Window(customtkinter.CTk):
    curr_img = None
    curr_photo_img = None

    def __init__(self, title, width, height, **kwargs):
        super().__init__(**kwargs)
        super().geometry(f'{width}x{height}')
        super().title(title)

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(1, weight=1)

        padding = 5

        self.controlFrame = customtkinter.CTkFrame(master=self)
        self.controlFrame.grid(row=0, column=0, padx=padding, pady=padding, sticky="nsew")
        self.controlFrame.grid_columnconfigure(0, weight=1)

        self.imageFrame = customtkinter.CTkScrollableFrame(master=self)
        self.imageFrame.grid(row=0, column=1, padx=padding, pady=padding, sticky="nsew")
        self.imageFrame.grid_columnconfigure(0, weight=1)
        self.imageFrame.grid_rowconfigure(0, weight=1)

        self.imageCanvas = customtkinter.CTkCanvas(master=self.imageFrame, width=1280, height=1000)
        self.imageCanvas.grid(row=0, column=0, sticky="nsew")
        self.imageCanvas.pack()

        self.blurController = customtkinter.CTkSlider(master=self.controlFrame,
                                                      command=self.onBlurControllerChanged, from_=0, to=100)
        self.blurController.grid(row=0, column=0, padx=padding, pady=padding, sticky="nsew")

        self.openImgBtn = customtkinter.CTkButton(master=self.controlFrame, text="Open image",
                                                  command=self.onOpenImgBtnClicked)
        self.openImgBtn.grid(row=1, column=0, padx=padding, pady=padding, sticky="nsew")

    def onBlurControllerChanged(self, value):
        global curr_img
        if curr_img is not None and isinstance(curr_img, Image.Image):
            modified_img = curr_img.filter(ImageFilter.GaussianBlur(radius=value))
            self._update_image(modified_img)

    def onOpenImgBtnClicked(self):
        filetypes = (
            ('JPG files', '*.JPG'),
            ('PNG files', '*.PNG')
        )

        filename = tkinter.filedialog.askopenfilename(
            title='Open a file',
            initialdir='./images',
            filetypes=filetypes
        )

        if filename != '':
            global curr_img
            curr_img = Image.open(filename)
            self._update_image(curr_img)

    def _update_image(self, image):
        global curr_photo_img
        if curr_img is not None and isinstance(image, Image.Image):
            curr_photo_img = ImageTk.PhotoImage(image)
            self.imageCanvas.config(height=image.height, width=image.width)
            self.imageCanvas.create_image(0, 0, anchor=NW, image=curr_photo_img)

    def start(self):
        super().mainloop()
