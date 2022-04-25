import itertools
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import numpy as np
import pandas

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import main


class ChooseVisual(tk.Frame):
    def __init__(self, parent, container, filename):
        super().__init__(container)

        self.parent = parent

        self.data = prepare_data(filename)

        # Back button
        self.back_button = ttk.Button(
            self,
            text="Back To Menu",
            command=lambda: self.parent.show_frame(main.Menu, filename, "normal")
        )

        ## Title label
        self.title_frame = tk.Frame(self)
        title = ttk.Label(
            self.title_frame,
            text='Choose Graph Type',
            font=("Helvetica", 25),
        )
        title.pack(expand=True)

        ## menu left
        self.buttons = tk.Frame(self, width=200)

        selected = {'fg': '#F0F0F0', 'bg': 'RoyalBlue3', 'activebackground':
            'gray71', 'activeforeground': 'gray71'}
        unselected = {'fg': 'black', 'bg': '#F0F0F0', 'activebackground':
            '#F0F0F0', 'activeforeground': '#F0F0F0'}

        bnt_list = []

        # PCA 2D button
        pca_2d = Button(
            self.buttons,
            text='2D PCA',
            command=lambda: [update(pca_2d)]
        )
        pca_2d.pack(expand=True)
        bnt_list.append(pca_2d)

        # PCA 3D button
        pca_3d = Button(
            self.buttons,
            text='3D PCA',
            command=lambda: [update(pca_3d)]
        )
        pca_3d.pack(expand=True)
        bnt_list.append(pca_3d)

        # KMeans button
        kmeans = Button(
            self.buttons,
            text='KMeans',
            command=lambda: [update(kmeans)]
        )
        kmeans.pack(expand=True)
        bnt_list.append(kmeans)

        # t-SNE button
        tsne = Button(
            self.buttons,
            text='t-SNE',
            command=lambda: [update(tsne)]
        )
        tsne.pack(expand=True)
        bnt_list.append(tsne)

        # image
        image = Image.open("Graphs/1-boxplot-dark.png")
        photo = ImageTk.PhotoImage(image)

        self.canvas_area = tk.Frame(self)
        # aa = Label(self.canvas_area, image=photo)
        # aa.image = photo
        # aa.pack(expand=True)
        self.canvas_area.grid(row=1)

        '''
        image = Image.open("Graphs/1-boxplot-dark.png")
        photo = ImageTk.PhotoImage(image)

        canvas_area = Label(self, image=photo)
        canvas_area.image = photo
        canvas_area.grid(row=1)
        '''

        # save
        self.save_button = Button(self, text="Save Image")

        self.back_button.grid(row=0, column=0, sticky="nsew")
        self.title_frame.grid(row=0, column=1, columnspan=2, pady=40, sticky="nsew")
        self.buttons.grid(row=1, column=0, padx=30, pady=30, rowspan=2, sticky="nsew")
        self.canvas_area.grid(row=1, column=1, sticky="nsew")
        self.save_button.grid(row=2, column=1, sticky="nsew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Change color of button to indicate which graph is being shown and clear canvas
        def update(clicked):
            for graph in self.canvas_area.winfo_children():
                graph.destroy()

            for button in bnt_list:
                if button == clicked:
                    button.configure(**selected)
                    if bnt_list.index(clicked) == 0:
                        graph = FigureCanvasTkAgg(pca_2d_graph(self.data), self.canvas_area)
                    elif bnt_list.index(clicked) == 1:
                        graph = FigureCanvasTkAgg(pca_3d_graph(self.data), self.canvas_area)
                    elif bnt_list.index(clicked) == 2:
                        graph = FigureCanvasTkAgg(kmeans_graph(self.data), self.canvas_area)
                    elif bnt_list.index(clicked) == 3:
                        graph = FigureCanvasTkAgg(tsne_graph(self.data), self.canvas_area)
                    graph.get_tk_widget().pack(side="top", fill="both", expand=True)
                else:
                    button.configure(**unselected)


class ChangeVisualiser(tk.Frame):
    def __init__(self, parent, container, data):
        super().__init__(container)

        self.data = data

        ## Title label
        self.title_frame = tk.Frame(self)
        title = ttk.Label(
            self.title_frame,
            text='Visualise Changes',
            font=("Helvetica", 25),
        )
        title.pack(expand=True)

        ## menu left
        self.buttons = tk.Frame(self, width=200)

        selected = {'fg': '#F0F0F0', 'bg': 'RoyalBlue3', 'activebackground':
            'gray71', 'activeforeground': 'gray71'}
        unselected = {'fg': 'black', 'bg': '#F0F0F0', 'activebackground':
            '#F0F0F0', 'activeforeground': '#F0F0F0'}

        bnt_list = []

        # PCA 2D button
        pca_2d = Button(
            self.buttons,
            text='2D PCA',
            command=lambda: [update(pca_2d)]
        )
        pca_2d.pack(expand=True)
        bnt_list.append(pca_2d)

        # PCA 3D button
        pca_3d = Button(
            self.buttons,
            text='3D PCA',
            command=lambda: [update(pca_3d)]
        )
        pca_3d.pack(expand=True)
        bnt_list.append(pca_3d)

        # KMeans button
        kmeans = Button(
            self.buttons,
            text='KMeans',
            command=lambda: [update(kmeans)]
        )
        kmeans.pack(expand=True)
        bnt_list.append(kmeans)

        # t-SNE button
        tsne = Button(
            self.buttons,
            text='t-SNE',
            command=lambda: [update(tsne)]
        )
        tsne.pack(expand=True)
        bnt_list.append(tsne)

        # image
        image = Image.open("Graphs/1-boxplot-dark.png")
        photo = ImageTk.PhotoImage(image)

        self.canvas_area = tk.Frame(self)
        # aa = Label(self.canvas_area, image=photo)
        # aa.image = photo
        # aa.pack(expand=True)
        self.canvas_area.grid(row=1)

        '''
        image = Image.open("Graphs/1-boxplot-dark.png")
        photo = ImageTk.PhotoImage(image)

        canvas_area = Label(self, image=photo)
        canvas_area.image = photo
        canvas_area.grid(row=1)
        '''

        # save
        self.save_button = Button(self, text="Save Image")

        self.title_frame.grid(row=0, column=0, columnspan=2, pady=40, sticky="nsew")
        self.buttons.grid(row=1, column=0, padx=30, pady=30, rowspan=2, sticky="nsew")
        self.canvas_area.grid(row=1, column=1, sticky="nsew")
        self.save_button.grid(row=2, column=1, sticky="nsew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Change color of button to indicate which graph is being shown and clear canvas
        def update(clicked):
            for graph in self.canvas_area.winfo_children():
                graph.destroy()

            for button in bnt_list:
                if button == clicked:
                    button.configure(**selected)
                    if bnt_list.index(clicked) == 0:
                        graph = FigureCanvasTkAgg(pca_2d_graph(self.data), self.canvas_area)
                    elif bnt_list.index(clicked) == 1:
                        graph = FigureCanvasTkAgg(pca_3d_graph(self.data), self.canvas_area)
                    elif bnt_list.index(clicked) == 2:
                        graph = FigureCanvasTkAgg(kmeans_graph(self.data), self.canvas_area)
                    elif bnt_list.index(clicked) == 3:
                        graph = FigureCanvasTkAgg(tsne_graph(self.data), self.canvas_area)
                    graph.get_tk_widget().pack(side="top", fill="both", expand=True)
                else:
                    button.configure(**unselected)

def prepare_data(filename):
    data_frame = pandas.read_sas(filename)
    data_frame.replace([np.inf, -np.inf], np.nan, inplace=True)
    data_frame.fillna(data_frame.mean(), inplace=True)
    return data_frame


def pca_2d_graph(df):
    print("pca 2d")

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
    pca_2d_graph = plt.figure(figsize=(7, 7))
    plt.scatter(x_3d[:, 0], x_3d[:, 1], alpha=0.1)

    plt.title('NHANES. PCA 2D projection', fontsize=20)
    plt.xlabel("First Principal Component", fontsize=14)
    plt.ylabel("Second Principal Component", fontsize=14)

    return pca_2d_graph


def pca_3d_graph(df):
    print("pca 3d")

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
    pca_2d_graph = plt.figure(figsize=(7, 7))
    plt.scatter(x_3d[:, 0], x_3d[:, 1], alpha=0.1)

    plt.title('NHANES. PCA 3D projection', fontsize=20)

    return pca_2d_graph


def kmeans_graph(df):
    print("kmeans")

    pca = PCA(2)
    # Transform the data
    data = pca.fit_transform(df)

    # Initialize the class object
    kmeans = KMeans(n_clusters=10)

    # predict the labels of clusters.
    label = kmeans.fit_predict(data)

    # Getting unique labels
    u_labels = np.unique(label)

    kmeans_graph = plt.figure(figsize=(12, 10))

    # plotting the results:
    for i in u_labels:
        plt.scatter(data[label == i, 0], data[label == i, 1], label="Cluster " + str(i))
    plt.legend()
    plt.show()

    plt.title('NHANES. KMeans projection', fontsize=20)
    plt.xlabel("First Principal Component", fontsize=14)
    plt.ylabel("Second Principal Component", fontsize=14)

    return kmeans_graph


def tsne_graph(df):
    print("t-sne")

    tsne = TSNE(random_state=17)

    X_tsne = tsne.fit_transform(df)

    tsne_graph = plt.figure(figsize=(12, 10))
    plt.scatter(X_tsne[:, 0], X_tsne[:, 1],
                edgecolor='none', alpha=0.7, s=40,
                cmap=plt.cm.get_cmap('nipy_spectral', 10))
    plt.colorbar()

    plt.title('NHANES. t-SNE projection', fontsize=20)
    plt.xlabel("t-SNE-x", fontsize=14)
    plt.ylabel("t-SNE-y", fontsize=14)

    return tsne_graph
