import cv2
import numpy as np
import os
import tqdm

if not (os.path.exists("../data/PolSAR_target")):
    os.mkdir("../data/PolSAR_target")
if not (os.path.exists("../data/PolSAR_source")):
    os.mkdir("../data/PolSAR_source")


pic_path = 'D:\\Project\\PolSAR-Speckle-Reduction-DeepLearning\\data\\PolSAR\\SF_2.png'  # 分割的图片的位置 @这是你需要修改的地方
pic_target = 'D:\\Project\\PolSAR-Speckle-Reduction-DeepLearning\\data\\PolSAR_target'  # 分割后的图片保存的文件夹 @这是你需要修改的地方
# 要分割后的尺寸
cut_width = 512
cut_length = 512
# 读取要分割的图片，以及其尺寸等数据
picture = cv2.imread(pic_path)
(width, length, depth) = picture.shape
# 预处理生成0矩阵
pic = np.zeros((cut_width, cut_length, depth))
# 计算可以划分的横纵的个数
num_width = int(width / cut_width)
num_length = int(length / cut_length)
# for循环迭代生成
for i in range(0, 20):
    for j in range(0, 20):
        # pic = picture[i * cut_width: (i + 1) * cut_width, j * cut_length: (j + 1) * cut_length, :]
        pic = picture[i*20: i*20 + cut_width, j*20: j*20 + cut_length, :]
        result_path = os.path.join(pic_target, '2_{}_{}.png'.format(i + 1, j + 1))
        cv2.imwrite(result_path, pic)

print("done!!!")
