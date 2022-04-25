import itertools
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ChooseVisual(tk.Frame):
    def __init__(self, parent, container, data):
        super().__init__(container)

        ## Title label
        self.title_frame = tk.Frame(self)
        title = ttk.Label(
            self.title_frame,
            text='Choose Visualisation',
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
            command=lambda: [update_style(0), self.pca_2d_graph(data, self.canvas_area)]
        )
        pca_2d.pack(expand=True)
        bnt_list.append(pca_2d)

        # PCA 3D button
        pca_3d = Button(
            self.buttons,
            text='3D PCA',
            command=lambda: [update_style(1), self.pca_3d_graph(data, self.canvas_area)]
        )
        pca_3d.pack(expand=True)
        bnt_list.append(pca_3d)

        # KMeans button
        kmeans = Button(
            self.buttons,
            text='KMeans',
            command=lambda: [update_style(2), self.kmeans_graph(data, self.canvas_area)]
        )
        kmeans.pack(expand=True)
        bnt_list.append(kmeans)

        # t-SNE button
        tsne = Button(
            self.buttons,
            text='t-SNE',
            command=lambda: [update_style(3), self.tsne_graph(data, self.canvas_area)]
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
        def update_style(clicked):
            for x in range(4):
                if x == clicked:
                    bnt_list[x].configure(**selected)
                else:
                    bnt_list[x].configure(**unselected)
            clear_canvas(self.canvas_area)

        def clear_canvas(canvas_area):
            for graph in canvas_area.winfo_children():
                graph.destroy()

    def pca_2d_graph(self, df, canvas_area):
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

        graph = FigureCanvasTkAgg(pca_2d_graph, canvas_area)
        graph.get_tk_widget().pack(side="top", fill="both", expand=True)

    def pca_3d_graph(self, df, canvas_area):
        print("pca 3d")

    def kmeans_graph(self, df, canvas_area):
        print("kmeans")

        # calling sklearn PCA
        pca = PCA(n_components=3)
        # fit X and apply the reduction to X
        x_3d = pca.fit_transform(df)

        # Set a 3 KMeans clustering
        kmeans = KMeans(n_clusters=3, random_state=0)
        # Compute cluster centers and predict cluster indices
        X_clustered = kmeans.fit_predict(x_3d)

        LABEL_COLOR_MAP = {0: 'r',
                           1: 'g',
                           2: 'b'}

        label_color = [LABEL_COLOR_MAP[l] for l in X_clustered]
        kmeans_graph = plt.figure(figsize=(7, 7))
        plt.scatter(x_3d[:, 0], x_3d[:, 1], c=label_color, alpha=0.1)

        graph = FigureCanvasTkAgg(kmeans_graph, canvas_area)
        graph.get_tk_widget().pack(side="top", fill="both", expand=True)

    def tsne_graph(self, df, canvas_area):
        print("t-sne")

        tsne = TSNE(random_state=17)

        X_tsne = tsne.fit_transform(df)

        tsne_graph = plt.figure(figsize=(12, 10))
        plt.scatter(X_tsne[:, 0], X_tsne[:, 1],
                    edgecolor='none', alpha=0.7, s=40,
                    cmap=plt.cm.get_cmap('nipy_spectral', 10))
        plt.colorbar()
        plt.title('NHANES. t-SNE projection');

        graph = FigureCanvasTkAgg(tsne_graph, canvas_area)
        graph.get_tk_widget().pack(side="top", fill="both", expand=True)
