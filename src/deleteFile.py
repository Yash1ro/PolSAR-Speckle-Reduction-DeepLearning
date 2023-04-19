import os


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

