import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import pattern_finder


class App(tk.Tk):
    def __init__(self):
        # configure the main window
        super().__init__()

        self.title("Pattern Finder")
        self.iconbitmap("icon.ico")

        # Window
        self.window_width = 800
        self.window_height = 500
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # find the center point
        center_x = int(screen_width / 2 - self.window_width / 2)
        center_y = int(screen_height / 2 - self.window_height / 2)
        # set the position of the window to the center of the screen
        self.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')

        # Creating a container
        self.container = tk.Frame(self, bg="#8AA7A9")
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.show_frame(HomePage, "", "normal")

    def show_frame(self, cont, filename, sc):
        """Method that shows the frame by putting the frame in front of the others"""
        self.state(sc)
        if cont == pattern_finder.ChooseVisual:
            frame = cont(self, self.container, filename)
        else:
            frame = cont(self, self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()  # This line will put the frame on front


class HomePage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        self.parent = parent

        # Title label
        title = ttk.Label(
            self,
            text='Tool To Find Patterns In Datasets',
            font=("Helvetica", 14))

        title.pack(ipadx=10, ipady=10)

        # Open file button
        open_button = ttk.Button(
            self,
            text='Open a File',
            command=self.select_file
        )
        open_button.pack(expand=True)

        # Choose example button
        test_button = ttk.Button(
            self,
            text='Example File',
            command=self.test_file
        )
        test_button.pack(expand=True)

        # Choose example button
        change_visual = ttk.Button(
            self,
            text='Choose Variables & Visualise Changes',
            command=lambda: self.parent.show_frame(pattern_finder.ChangeVisualiser, "", "zoomed")
        )
        change_visual.pack(expand=True)

    def select_file(self):
        """Change to choose visual frame and set file to selected file"""
        filetypes = [('DataFormat Files', '*.xpt')]

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        if filename != "":
            showinfo(
                title='Selected File',
                message=filename
            )
            self.parent.show_frame(pattern_finder.ChooseVisual, filename, "zoomed")

    def test_file(self):
        """Change to choose visual frame and set file to default"""
        filename = "D:/Documents/GitHub/Project Stuff/WebScraper/NHANES/Demographics/DEMO_H.XPT"
        self.parent.show_frame(pattern_finder.ChooseVisual, filename, "zoomed")


if __name__ == "__main__":
    app = App()
    app.mainloop()
