
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 数据加载


data = pd.read_csv('CarPrice_A.csv',encoding='gbk')

#方法1：使用所有numeric 数据分类
#train_x = data[["wheelbase", "carlength", "carwidth", "carheight", "curbweight", "enginesize","boreratio","stroke",	"compressionratio","horsepower","peakrpm","citympg","highwaympg","price"]]

#方法2： 车型尺寸类各指标及动力性能类各指标有高度相关性，因此，选择车型长度、动力、价格三指标聚类
train_x = data[["carlength", "horsepower","price"]]
# LabelEncoder

# 规范化到 [0,1] 空间

min_max_scaler = preprocessing.MinMaxScaler()

train_x = min_max_scaler.fit_transform(train_x)

pd.DataFrame(train_x).to_csv('temp.csv', index=False)
# print(train_x)


### 使用KMeans聚类

kmeans = KMeans(n_clusters=40)

kmeans.fit(train_x)

predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中

result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)

result.rename({0: u'cluster'}, axis=1, inplace=True)

print(result)
# 将结果导出到CSV文件中

result.to_csv("车型聚类三指标40类.csv",index=False)

# 结论：根据三指标聚类比根据所有指标聚类更具参考意义。

