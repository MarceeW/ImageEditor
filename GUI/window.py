import customtkinter


class Window(customtkinter.CTk):
    def __init__(self, title, width, height, **kwargs):
        super().__init__(**kwargs)
        super().geometry(f'{width}x{height}')
        super().title(title)

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        padding = 5

        self.controlFrame = customtkinter.CTkFrame(master=self)
        self.controlFrame.grid(row=0, column=0, padx=padding, pady=padding, sticky="nsew")

        self.imageFrame = customtkinter.CTkFrame(master=self)
        self.imageFrame.grid(row=0, column=1, padx=padding, pady=padding, sticky="nsew")

        self.blurController = customtkinter.CTkSlider(master=self.controlFrame,command=self.onBlurControllerChanged)
        self.blurController.grid(row=0, column=1, padx=padding, pady=padding, sticky="nsew")

    def onBlurControllerChanged(self,value):
        print(value)

    def start(self):
        super().mainloop()
