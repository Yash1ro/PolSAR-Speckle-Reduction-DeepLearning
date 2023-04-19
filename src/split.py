import os
import random
import shutil


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


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
    dest_dir_train = '../data/train_Pauli'  # 这个文件夹需要提前建好
    dest_dir_val = '../data/val_Pauli'
    dest_dir_test = '../data/test_Pauli'

    img_list_origin = get_imlist(src_path)
    img_list = get_imlist(src_path)
    random.shuffle(img_list)
    le = int(len(img_list_origin) * 0.7)  # 这个可以修改划分比例
    for f in img_list[:le]:
        shutil.move(f, dest_dir_train)

    img_list = get_imlist(src_path)
    random.shuffle(img_list)
    le = int(len(img_list_origin) * 0.2)  # 这个可以修改划分比例
    for f in img_list[:le]:
        shutil.move(f, dest_dir_val)

    img_list = get_imlist(src_path)
    random.shuffle(img_list)
    le = int(len(img_list_origin) * 0.1)  # 这个可以修改划分比例
    for f in img_list[:le]:
        shutil.move(f, dest_dir_test)


del_files2('../data/train_Pauli')
del_files2('../data/val_Pauli')
del_files2('../data/test_Pauli')
getData('../data/Pauli_data')
