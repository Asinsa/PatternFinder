import itertools
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ChooseVisual(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        data = None

        ## Title label
        title_frame = tk.Frame(self)
        title = ttk.Label(
            title_frame,
            text='Choose Visualisation',
            font=("Helvetica", 25),
        )
        title.pack(expand=True)

        ## menu left
        buttons = tk.Frame(self, width=200)

        selected = {'fg': '#F0F0F0', 'bg': 'RoyalBlue3', 'activebackground':
            'gray71', 'activeforeground': 'gray71'}
        unselected = {'fg': 'black', 'bg': '#F0F0F0', 'activebackground':
            '#F0F0F0', 'activeforeground': '#F0F0F0'}

        bnt_list = []

        # PCA 2D button
        pca_2d = Button(
            buttons,
            text='2D PCA',
            command=lambda:[pca_2d_graph(), update_style(0)]
        )
        pca_2d.pack(expand=True)
        bnt_list.append(pca_2d)


        # PCA 3D button
        pca_3d = Button(
            buttons,
            text='3D PCA',
            command=lambda:[pca_3d_graph(), update_style(1)]
        )
        pca_3d.pack(expand=True)
        bnt_list.append(pca_3d)

        # KMeans button
        kmeans = Button(
            buttons,
            text='KMeans',
            command=lambda:[kmeans_graph(), update_style(2)]
        )
        kmeans.pack(expand=True)
        bnt_list.append(kmeans)

        # t-SNE button
        tsne = Button(
            buttons,
            text='t-SNE',
            command=lambda:[tsne_graph(), update_style(3)]
        )
        tsne.pack(expand=True)
        bnt_list.append(tsne)

        # image
        image = Image.open("Graphs/1-boxplot-dark.png")
        photo = ImageTk.PhotoImage(image)

        canvas_area = Label(self, image=photo)
        canvas_area.image = photo
        canvas_area.grid(row=1)

        # save
        save_button = Button(self, text="Save Image")

        title_frame.grid(row=0, column=0, columnspan=2, pady=40, sticky="nsew")
        buttons.grid(row=1, column=0, padx=30, pady=30, rowspan=2, sticky="nsew")
        canvas_area.grid(row=1, column=1, sticky="nsew")
        save_button.grid(row=2, column=1, sticky="nsew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Define a function to update the button style
        def update_style(clicked):
            for x in range(4):
                if x == clicked:
                    bnt_list[x].configure(**selected)
                else:
                    bnt_list[x].configure(**unselected)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data


def pca_2d_graph():
    print("pca 2d")


    '''
    features = (list(df.columns))

    # 3.2 PCA With Color
    color_features = []
    for i in df.columns:
        if 'color' in i:
            color_features.append(i)
    # create our color dataframe and inspect first 5 rows with head()
    data_color = df[color_features]
    data_color.head()

    X = data_color.values
    # calling sklearn PCA
    pca = PCA(n_components=3)
    # fit X and apply the reduction to X
    x_3d = pca.fit_transform(df)

    # Let's see how it looks like in 2D - could do a 3D plot as well
    plt.figure(figsize=(7, 7))
    plt.scatter(x_3d[:, 0], x_3d[:, 1], alpha=0.1)
    plt.show()

    figure = plt.Figure(figsize=(6, 5), dpi=100)
    chart_type = FigureCanvasTkAgg(figure, vis_menu)
    chart_type.get_tk_widget().pack()
    '''


def pca_3d_graph():
    print("pca 3d")


def kmeans_graph():
    print("kmeans")


def tsne_graph():
    print("t-sne")
