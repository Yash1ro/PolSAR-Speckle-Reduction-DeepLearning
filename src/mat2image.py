import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy.linalg

# 读取HDF5文件
with h5py.File('../data/oriData.mat', 'r') as f:
    data_paris = f['ParisExperimentT'][:]
    data_sanfran = f['SanFranExperimentT'][:]

# 对数据进行T矩阵分解
T_paris = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
T_sanfran = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
L_paris, U_paris, P_paris = scipy.linalg.lu(T_paris)
L_sanfran, U_sanfran, P_sanfran = scipy.linalg.lu(T_sanfran)
T_inv_paris = scipy.linalg.solve(U_paris, scipy.linalg.solve(L_paris, P_paris.T))
T_inv_sanfran = scipy.linalg.solve(U_sanfran, scipy.linalg.solve(L_sanfran, P_sanfran.T))
S_paris = np.dot(np.dot(T_inv_paris, data_paris), T_inv_paris.conj().T)
S_sanfran = np.dot(np.dot(T_inv_sanfran, data_sanfran), T_inv_sanfran.conj().T)

# 生成Pauli图像
HH_paris = S_paris[0, 0, :, :]
HV_paris = S_paris[0, 1, :, :]
VV_paris = S_paris[1, 1, :, :]
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
axs[0].imshow(np.abs(HH_paris), cmap='gray')
axs[0].set_title('HH')
axs[1].imshow(np.abs(VV_paris), cmap='gray')
axs[1].set_title('VV')
axs[2].imshow(np.abs(HV_paris), cmap='gray')
axs[2].set_title('HV')
plt.show()

HH_sanfran = S_sanfran[0, 0, :, :]
HV_sanfran = S_sanfran[0, 1, :, :]
VV_sanfran = S_sanfran[1, 1, :, :]
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
axs[0].imshow(np.abs(HH_sanfran), cmap='gray')
axs[0].set_title('HH')
axs[1].imshow(np.abs(VV_sanfran), cmap='gray')
axs[1].set_title('VV')
axs[2].imshow(np.abs(HV_sanfran), cmap='gray')
axs[2].set_title('HV')
plt.show()
