import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import h5py

with h5py.File('../data/oriData.mat', 'r') as f:
    paris_t = f['ParisExperimentT'][()]
    sanfran_t = f['SanFranExperimentT'][()]

# 计算Pauli分解矩阵
pauli_mat = np.zeros((3, 3), dtype=np.complex64)
pauli_mat[0, 1] = pauli_mat[1, 0] = 1
pauli_mat[0, 2] = pauli_mat[2, 0] = 1j
pauli_mat[1, 2] = pauli_mat[2, 1] = -1j

# 计算Pauli分解结果
paris_pauli = np.zeros_like(paris_t)
sanfran_pauli = np.zeros_like(sanfran_t)
for i in range(paris_t.shape[0]):
    for j in range(paris_t.shape[1]):
        pauli_vec = np.dot(pauli_mat, np.dot(paris_t[i, j], pauli_mat.T.conj()))
        paris_pauli[i, j] = pauli_vec
for i in range(sanfran_t.shape[0]):
    for j in range(sanfran_t.shape[1]):
        pauli_vec = np.dot(pauli_mat, np.dot(sanfran_t[i, j], pauli_mat.T.conj()))
        sanfran_pauli[i, j] = pauli_vec

# 取模计算强度
paris_intensity = np.abs(paris_pauli)**2
sanfran_intensity = np.abs(sanfran_pauli)**2

# 绘制Pauli图
plt.figure()
plt.imshow(np.hstack([paris_intensity, sanfran_intensity]), cmap='gray')
plt.axis('off')
plt.show()
