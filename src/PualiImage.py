import h5py
import numpy as np
import matplotlib.pyplot as plt
import cv2
import torch

# 读取HDF5格式文件
with h5py.File('../data/PauliImage.mat', 'r') as f:
    # 读取数据集
    paris_data = np.array(f['Paris'])
    sanfran_data = np.array(f['SanFran'])

    # 输出数据集形状
    print('Paris dataset shape:', paris_data.shape)
    print('San Francisco dataset shape:', sanfran_data.shape)
    print((paris_data.T).shape)

    # 绘制数据集图形
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.imshow(paris_data.T)
    ax1.set_title('Paris dataset')
    ax2.imshow(sanfran_data.T)
    ax2.set_title('San Francisco dataset')
    plt.imsave('Paris_experiment.png', paris_data.T)
    plt.imsave('SanFran_experiment.png', sanfran_data.T)
    plt.show()
