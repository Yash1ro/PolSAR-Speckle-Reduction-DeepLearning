import os
import random
import shutil
from tqdm import tqdm


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]


# 删除文件夹
def del_files2(dir_path):
    for root, dirs, files in os.walk(dir_path, topdown=False):
        print(root)  # 各级文件夹绝对路径
        print(dirs)  # root下一级文件夹名称列表，如 ['文件夹1','文件夹2']
        print(files)  # root下文件名列表，如 ['文件1','文件2']
        # 第一步：删除文件
        for name in files:
            os.remove(os.path.join(root, name))  # 删除文件
        # 第二步：删除空文件夹
        for name in dirs:
            os.rmdir(os.path.join(root, name))  # 删除一个空目录


def getData(src_path):
    dest_dir_train_1 = '../data/train_SAR'  # 这个文件夹需要提前建好
    dest_dir_val_1 = '../data/val_SAR'
    dest_dir_test_1 = '../data/test_SAR'

    dest_dir_train_2 = '../data/train_Pauli'  # 这个文件夹需要提前建好
    dest_dir_val_2 = '../data/val_Pauli'
    dest_dir_test_2 = '../data/test_Pauli'

    if 'SAR' in src_path:
        img_list_origin = get_imlist(src_path)
        img_list = get_imlist(src_path)
        random.shuffle(img_list)
        le = int(len(img_list_origin) * 0.8)  # 这个可以修改划分比例
        for f in tqdm(img_list[:le]):
            shutil.move(f, dest_dir_train_1)
        print("Training set has been done !")

        img_list = get_imlist(src_path)
        random.shuffle(img_list)
        le = int(len(img_list_origin) * 0.19)  # 这个可以修改划分比例
        for f in tqdm(img_list[:le]):
            shutil.move(f, dest_dir_val_1)
        print("Valuating set has been done !")

        img_list = get_imlist(src_path)
        random.shuffle(img_list)
        le = int(len(img_list_origin) * 0.01)  # 这个可以修改划分比例
        for f in tqdm(img_list[:le]):
            shutil.move(f, dest_dir_test_1)
        print("Testing set has been done !")
    elif 'Pauli' in src_path:
        img_list_origin = get_imlist(src_path)
        img_list = get_imlist(src_path)
        random.shuffle(img_list)
        le = int(len(img_list_origin) * 0.8)  # 这个可以修改划分比例
        for f in tqdm(img_list[:le]):
            shutil.move(f, dest_dir_train_2)
        print("Training set has been done !")

        img_list = get_imlist(src_path)
        random.shuffle(img_list)
        le = int(len(img_list_origin) * 0.19)  # 这个可以修改划分比例
        for f in tqdm(img_list[:le]):
            shutil.move(f, dest_dir_val_2)
        print("Valuating set has been done !")

        img_list = get_imlist(src_path)
        random.shuffle(img_list)
        le = int(len(img_list_origin) * 0.01)  # 这个可以修改划分比例
        for f in tqdm(img_list[:le]):
            shutil.move(f, dest_dir_test_2)
        print("Testing set has been done !")
