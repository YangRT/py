from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy
from matplotlib.colors import ListedColormap
f = open("dataset3.txt", 'r',encoding='utf-8')
data = []
type = []
for line in f.readlines():
    item = line.split(',')
    x = float(item[0])
    y = float(item[1])
    type.append(int(item[2])-1)
    t = [x, y]
    data.append(t)
X = numpy.array(data)
k = KMeans(n_clusters=5,).fit(X)
label = k.labels_
print(label)
print(type)
colors = ListedColormap(['#FF0000','#00FF00','#0000FF','#000000','#ffcb00'])
plt.scatter(X[:,0:1],X[:,1:2],c=label,cmap=colors)
plt.show()
# 数据自带分类
plt.scatter(X[:,0:1],X[:,1:2],c=type,cmap=colors)
plt.show()
# DBSCAN 算法
y_pred = DBSCAN(eps = 0.1, min_samples = 15).fit_predict(X)
plt.scatter(X[:, 0:1], X[:, 1:2], c=y_pred,cmap=colors)
plt.show()

