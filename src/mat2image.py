import h5py

# 加载mat文件
data = h5py.File('../data/oriData.mat')

# 访问mat文件中的数据
data_array = data['ParisExperimentT']

# 打印数组的形状
print(data_array.shape)
