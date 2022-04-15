import tkinter
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def main_menu():
    # Window
    window_width = 800
    window_height = 500
    # get the screen dimension
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # set the position of the window to the center of the screen
    main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Title label
    title = ttk.Label(
        main,
        text='Tool To Find Patterns In Datasets',
        font=("Helvetica", 14))

    title.pack(ipadx=10, ipady=10)

    # Open file button
    open_button = ttk.Button(
        main,
        text='Open a File',
        command=select_file
    )

    open_button.pack(expand=True)

    # Choose example button
    test_button = ttk.Button(
        main,
        text='Example File',
        command=test_file
    )

    test_button.pack(expand=True)


def select_file():
    filetypes = filetypes = [('DataFormat Files', '*.xpt')]

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if filename != "":
        showinfo(
            title='Selected File',
            message=filename
        )

        choose_visualisation(filename)
        main.quit()


def test_file():
    choose_visualisation("D:/Documents/GitHub/Project Stuff/WebScraper/NHANES/2013/Demographics/DEMO_H.XPT")
    main.quit()


def choose_visualisation(filename):
    vis_menu = tkinter.Tk()
    vis_menu.title("Pattern Finder")
    vis_menu.iconbitmap("icon.ico")
    vis_menu.state('zoomed')

    # Title label
    title = ttk.Label(
        vis_menu,
        text='Choose Visualisation',
        font=("Helvetica", 14))
    title.pack(ipadx=10, ipady=10)



    vis_menu.mainloop()


main = tkinter.Tk()
main.title("Pattern Finder")
main.iconbitmap("icon.ico")

main_menu()

main.mainloop()
