import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = pandas.read_sas('NHANES/2017/Demographics/DEMO_J.xpt')
#for chunk in data:
#    print(chunk)

features = (list(data.columns))

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

finalDf = pandas.concat([principalDf, data[['target']]], axis=1)


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
import xport

with open('NHANES/2017/Demographics/DEMO_J.xpt', 'rb') as f:
    for row in xport.Reader(f):
        print(row)

'''

'''


import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names


pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

# Percentage of variance explained for each components
print(
    "explained variance ratio (first two components): %s"
    % str(pca.explained_variance_ratio_)
)

plt.figure()
colors = ["navy", "turquoise", "darkorange"]
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(
        X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name
    )
plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("PCA of IRIS dataset")

plt.show()
'''