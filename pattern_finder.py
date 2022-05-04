import itertools
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import numpy as np
import pandas
import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import main


class ChooseVisual(tk.Frame):
    def __init__(self, parent, container, filename):
        super().__init__(container)

        self.data = prepare_data(filename)
        self.name = Path(filename).stem

        # Back button
        self.back_button = ttk.Button(
            self,
            text="Back To Home",
            command=lambda: parent.show_frame(main.HomePage, "", "normal")
        )

        # Title label
        self.title_frame = tk.Frame(self)
        title = ttk.Label(
            self.title_frame,
            text='Choose Graph Type',
            font=("Helvetica", 25),
        )
        title.pack(expand=True)

        # Menu left
        self.buttons = tk.Frame(self, width=200)

        selected = {'fg': '#F0F0F0', 'bg': 'RoyalBlue3', 'activebackground':
            'gray71', 'activeforeground': 'gray71'}
        unselected = {'fg': 'black', 'bg': '#F0F0F0', 'activebackground':
            '#F0F0F0', 'activeforeground': '#F0F0F0'}

        bnt_list = []

        # Correlation button
        corr = Button(
            self.buttons,
            text='Correlation Heat Map',
            command=lambda: [update(corr)]
        )
        corr.pack(expand=True)
        bnt_list.append(corr)

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
            """Update the canvas"""
            for graph in self.canvas_area.winfo_children():
                graph.destroy()

            for button in bnt_list:
                if button == clicked:
                    button.configure(**selected)
                    if bnt_list.index(clicked) == 0:
                        graph = FigureCanvasTkAgg(correlation(self.data, self.name), self.canvas_area)
                    elif bnt_list.index(clicked) == 1:
                        graph = FigureCanvasTkAgg(pca_2d_graph(self.data, self.name), self.canvas_area)
                    elif bnt_list.index(clicked) == 2:
                        graph = FigureCanvasTkAgg(pca_3d_graph(self.data, self.name), self.canvas_area)
                    elif bnt_list.index(clicked) == 3:
                        graph = FigureCanvasTkAgg(kmeans_graph(self.data, self.name), self.canvas_area)
                    elif bnt_list.index(clicked) == 4:
                        graph = FigureCanvasTkAgg(tsne_graph(self.data, self.name), self.canvas_area)
                    graph.get_tk_widget().pack(side="top", fill="both", expand=True)
                else:
                    button.configure(**unselected)


class ChangeVisualiser(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        # Back button
        self.back_button = ttk.Button(
            self,
            text="Back To Home",
            command=lambda: parent.show_frame(main.HomePage, "", "normal")
        )

        # Title label
        self.title_frame = tk.Frame(self)
        title = ttk.Label(
            self.title_frame,
            text='Visualise Changes',
            font=("Helvetica", 25),
        )
        title.pack(expand=True)

        # Menu left
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

        # middle area
        image = Image.open("Graphs/1-boxplot-dark.png")
        photo = ImageTk.PhotoImage(image)

        self.canvas_area = Label(self, image=photo)
        self.canvas_area.image = photo
        self.canvas_area.grid(row=1)

        # right area
        self.dropdowns = tk.Frame(self, width=200)

        self.categories = ('Demographics', 'Dietary', 'Examination', 'Laboratory', 'Questionnaire')
        self.clicked_category = tk.StringVar(self)
        self.category = ttk.OptionMenu(self.dropdowns, self.clicked_category, self.categories[0], *self.categories)
        self.category.pack(expand=True)

        self.types = ("DEMO", 'Demographics', 'Dietary', 'Examination', 'Laboratory', 'Questionnaire')

        self.clicked_type = tk.StringVar(self)
        self.type = ttk.OptionMenu(self.dropdowns, self.clicked_type, self.types[0], *self.types)
        self.type.pack(expand=True)

        # year slider
        self.slider = Scale(self, from_=1999, to=2015, tickinterval=2, orient=HORIZONTAL)

        # save
        self.save_button = Button(self, text="Save Image")

        self.back_button.grid(row=0, column=0, sticky="nsew")
        self.title_frame.grid(row=0, column=1, columnspan=2, pady=40, sticky="nsew")
        self.buttons.grid(row=1, column=0, padx=30, pady=30, rowspan=2, sticky="nsew")
        self.canvas_area.grid(row=1, column=1, rowspan=2, sticky="nsew")
        self.dropdowns.grid(row=1, column=2, padx=30, pady=30, rowspan=2, sticky="nsew")
        self.slider.grid(row=2, column=1, padx=20, pady=40, sticky="ew")
        self.save_button.grid(row=3, column=1, sticky="nsew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Change color of button to indicate which graph is being shown and clear canvas
        def update(clicked):
            """Update the canvas"""
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
    """Return the dataframe"""
    data_frame = pandas.read_sas(filename)
    data_frame.replace([np.inf, -np.inf], np.nan, inplace=True)
    data_frame.fillna(data_frame.mean(), inplace=True)
    return data_frame


# Method that returns a heatmap showing correlations
def correlation(df, filename):
    """Return the correlation heat map"""
    # Plotting the graph
    heat_map = plt.figure(figsize=(12, 10))
    cor = df.corr()
    sns.heatmap(cor, annot=False, cmap=plt.cm.Reds)

    # Labelling graph
    plt.title('Correlation Heat Map Of ' + filename, fontsize=20)
    plt.xlabel("Variables", fontsize=14)
    plt.ylabel("Variables", fontsize=14)

    return heat_map


# Method that returns a PCA 2D graph
def pca_2d_graph(df, filename):
    """Return the PCA 2D graph"""
    # Create color dataframe and inspect first 5 rows with head()
    color_features = []
    for i in df.columns:
        if 'color' in i:
            color_features.append(i)
    data_color = df[color_features]
    data_color.head()

    # Perform PCA with 2 principal components
    pca = PCA(n_components=2)
    X = pca.fit_transform(df)

    # Plotting the graph
    pca_2d_graph = plt.figure(figsize=(7, 7))
    plt.scatter(X[:, 0], X[:, 1], alpha=0.1)

    # Label graph
    plt.title('PCA 2D Projection Of ' + filename, fontsize=20)
    plt.xlabel("First Principal Component", fontsize=14)
    plt.ylabel("Second Principal Component", fontsize=14)

    return pca_2d_graph


# Method that returns a PCA 3D graph
def pca_3d_graph(df, filename):
    """Return the PCA 3D graph"""
    sns.set_style("white")

    # Perform PCA with 3 principle components
    pca = PCA(n_components=3)
    pca.fit(df)

    # Store results of PCA in a data frame
    result = pandas.DataFrame(pca.transform(df), columns=['PCA%i' % i for i in range(3)], index=df.index)

    # Plotting the graph
    pca_3d_graph = plt.figure()
    ax = pca_3d_graph.add_subplot(111, projection='3d')
    ax.scatter(result['PCA0'], result['PCA1'], result['PCA2'], cmap="Set2_r", s=60)

    # Label graph
    plt.title('PCA 3D Projection Of ' + filename, fontsize=20)
    ax.set_xlabel("First Principal Component")
    ax.set_ylabel("Second Principal Component")
    ax.set_zlabel("Third Principal Component")

    return pca_3d_graph


# Method that returns a K-means graph
def kmeans_graph(df, filename):
    """Return the K-means graph"""
    # Perform PCA with 2 principle components
    pca = PCA(n_components=2)
    data = pca.fit_transform(df)

    # Set the number of clusters & predict them
    kmeans = KMeans(n_clusters=10)
    label = kmeans.fit_predict(data)

    # Get unique labels
    u_labels = np.unique(label)

    # Plotting the graph
    kmeans_graph = plt.figure(figsize=(12, 10))
    for i in u_labels:
        plt.scatter(data[label == i, 0], data[label == i, 1], label="Cluster " + str(i))

    # Label graph
    plt.legend()
    plt.title('KMeans Projection Of ' + filename, fontsize=20)
    plt.xlabel("First Principal Component", fontsize=14)
    plt.ylabel("Second Principal Component", fontsize=14)

    return kmeans_graph


# Method that returns a t-SNE graph
def tsne_graph(df, filename):
    """Return the t-SNE graph"""
    # Perform t-SNE
    tsne = TSNE(random_state=17)
    X_tsne = tsne.fit_transform(df)

    # Plotting the graph
    tsne_graph = plt.figure(figsize=(12, 10))
    plt.scatter(X_tsne[:, 0], X_tsne[:, 1],
                edgecolor='none', alpha=0.7, s=40,
                cmap=plt.cm.get_cmap('nipy_spectral', 10))
    plt.colorbar()

    # Label graph
    plt.title('t-SNE Projection Of ' + filename, fontsize=20)
    plt.xlabel("t-SNE-x", fontsize=14)
    plt.ylabel("t-SNE-y", fontsize=14)

    return tsne_graph
