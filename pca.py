import matplotlib
import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# Importing Modules
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

df = pandas.read_sas('NHANES/2017/Demographics/DEMO_J.xpt')
#df = pandas.read_sas('NHANES/2017/Dietary/DR1IFF_J.xpt')
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.mean(), inplace=True)

#for chunk in df:
#    print(chunk)

features = (list(df.columns))

'''
#DONT DELETE
#THIS IS SCATTER PLOT OF ALL THE DATA BEFORE PCA

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import scale

df_scaled = scale(df[features])
df2 = pandas.DataFrame(df_scaled, columns=features)
df2['SEQN'] = pandas.Series(df['SEQN'], index=df.index)
df3 = pandas.melt(df2, id_vars='SEQN', value_vars=df2[features])
'''

'''
# 1. Box Plot
plt.figure(figsize=(8,6))
sns.set(style="darkgrid")
sns.boxplot(y='variable',x='value', data=df3, palette="Set2")
plt.show()
'''

'''
# 2. Scary looking heat map
plt.figure(figsize=(8,6))
sns.set(style="whitegrid")
sns.heatmap(df2[features].corr(method='pearson'), vmin=-.1, vmax=1,  annot=True, cmap='RdYlGn')
plt.show()
'''

'''
# 3. PCA Scatter Graph
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(df)

print('Projecting %d-dimensional data to 2D' % df.shape[1])

plt.figure(figsize=(12,10))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1],
            edgecolor='none', alpha=0.7, s=40,
            cmap=plt.cm.get_cmap('nipy_spectral', 10))
plt.colorbar()
plt.title('NHANES. PCA projection')
plt.show()
'''

'''
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
plt.figure(figsize = (7,7))
plt.scatter(x_3d[:,0],x_3d[:,1], alpha=0.1)
plt.show()
'''

# 3.3.1 PCA and KMeans but rainbowz
pca = PCA(2)

# Transform the data
data = pca.fit_transform(df)

# Import KMeans module
from sklearn.cluster import KMeans

# Initialize the class object
kmeans = KMeans(n_clusters=10)

# predict the labels of clusters.
label = kmeans.fit_predict(data)

# Getting unique labels
u_labels = np.unique(label)

# plotting the results:
for i in u_labels:
    plt.scatter(data[label == i, 0], data[label == i, 1], label="Cluster " + str(i))
plt.legend()
plt.show()


'''
# 3.3.2 PCA and KMeans
from sklearn.cluster import KMeans

# calling sklearn PCA
pca = PCA(n_components=3)
# fit X and apply the reduction to X
x_3d = pca.fit_transform(df)

# Set a 3 KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
# Compute cluster centers and predict cluster indices
X_clustered = kmeans.fit_predict(x_3d)

LABEL_COLOR_MAP = {0 : 'r',
                   1 : 'g',
                   2 : 'b'}

label_color = [LABEL_COLOR_MAP[l] for l in X_clustered]
plt.figure(figsize = (7,7))
plt.scatter(x_3d[:,0],x_3d[:,1], c= label_color, alpha=0.1)
plt.show()
'''


'''
# 4. t-SNE Scatter graph
from sklearn.manifold import TSNE
tsne = TSNE(random_state=17)

X_tsne = tsne.fit_transform(df)

plt.figure(figsize=(12,10))
plt.scatter(X_tsne[:, 0], X_tsne[:, 1],
            edgecolor='none', alpha=0.7, s=40,
            cmap=plt.cm.get_cmap('nipy_spectral', 10))
plt.colorbar()
plt.title('NHANES. t-SNE projection');
plt.show()
'''



'''
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

pca = df.PCA(
     n_components=6,
     n_iter=10,
     rescale_with_mean=False,
     rescale_with_std=False,
     copy=True,
     check_input=True,
     engine='sklearn',
     random_state=234
 )
pca = pca.fit(df2[features])

kmeans5 = KMeans(n_clusters=5, init='random', n_init=20, max_iter=600,  random_state=234)
kmeans5.fit_predict(df2[features])
df2['Kcluster'] =  pandas.Series(kmeans5.labels_, index=df.index)
ax = pca.plot_row_coordinates(
     df2[features],
     ax=None,
     figsize=(10, 8),
     x_component=0,
     y_component=1,
     labels=None,
     color_labels=df2['Kcluster'],
     ellipse_outline=True,
     ellipse_fill=True,
     show_points=True
 ).legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Row Principal Components with KMeans Cluster Groups', fontsize=18)
plt.xlabel('Component 1 (50% Intertia)',fontsize=18)
plt.ylabel('Component 2 (24% Intertia)', fontsize=18)
plt.show()
'''


'''
# 1. Standardising the data
# Separating out the features
x = data.loc[:, features].values
# Separating out the target
#y = data.loc[:, ['target']].values
# Standardizing the features
x = StandardScaler().fit_transform(x)


# 2. PCA Projection to 2D
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pandas.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])

#finalDf = pandas.concat([principalDf, data[['target']]], axis=1)


# 3. Visualise 2D Projection
plt.figure()
plt.figure(figsize=(10, 10))
plt.xticks(fontsize=12)
plt.yticks(fontsize=14)
plt.xlabel('Principal Component - 1', fontsize=20)
plt.ylabel('Principal Component - 2', fontsize=20)
plt.title("Principal Component Analysis of Demographics", fontsize=20)
targets = ['DMDEDUC2', 'DMQMILIZ']
colors = ['r', 'g']
for target, color in zip(targets, colors):
    indicesToKeep = data['label'] == target
    plt.scatter(principalDf.loc[indicesToKeep, 'principal component 1']
               , principalDf.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)

plt.legend(targets,prop={'size': 15})
'''