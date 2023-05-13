import os
from torchvision import transforms
from PIL import Image
import myLogs as m
from tqdm import tqdm
import split


if __name__ == "__main__":
    if not (os.path.exists("../data/train_SAR")):
        os.mkdir("../data/train_SAR")
    if not (os.path.exists("../data/val_SAR")):
        os.mkdir("../data/val_SAR")
    if not (os.path.exists("../data/test_SAR")):
        os.mkdir("../data/test_SAR")
    if not (os.path.exists("../data/SAR_data")):
        os.mkdir("../data/SAR_data")

    if not (os.path.exists("../data/train_Pauli")):
        os.mkdir("../data/train_Pauli")
    if not (os.path.exists("../data/val_Pauli")):
        os.mkdir("../data/val_Pauli")
    if not (os.path.exists("../data/test_Pauli")):
        os.mkdir("../data/test_Pauli")
    if not (os.path.exists("../data/Pauli_data")):
        os.mkdir("../data/Pali_data")

    split.del_files2('../data/SAR_data')
    split.del_files2('../data/train_SAR')
    split.del_files2('../data/val_SAR')
    split.del_files2('../data/test_SAR')

    split.del_files2('../data/Pauli_data')
    split.del_files2('../data/train_Pauli')
    split.del_files2('../data/val_Pauli')
    split.del_files2('../data/test_Pauli')

    # 指定文件路径
    root_path = "../data"
    target_path_1 = "SARImage"
    target_path_2 = "PauliImage"

    # 获取文件列表
    img_list_1 = os.listdir(os.path.join(root_path, target_path_1))
    img_list_2 = os.listdir(os.path.join(root_path, target_path_2))

    # 创建transform对象
    trans_rancrop_1 = transforms.RandomCrop(512)
    trans_rancrop_2 = transforms.RandomCrop(256)


    # 创建数据集
    if len(os.listdir("../data/SAR_data")) == 0:
        for i in tqdm(img_list_1):
            img = Image.open(os.path.join(root_path, target_path_1, i))
            print(img)

            for k in tqdm(range(800)):
                img_crop = trans_rancrop_2(img)
                img_crop.save("../data/SAR_data/{}_{}.png".format(i.split(".png")[0], k))

        print("SAR IS DONE!")


    if len(os.listdir("../data/Pauli_data")) == 0:
        for i in tqdm(img_list_2):
            img = Image.open(os.path.join(root_path, target_path_2, i))
            print(img)

            for k in tqdm(range(800)):
                img_crop = trans_rancrop_1(img)
                img_crop.save("../data/Pauli_data/{}_{}.png".format(i.split(".png")[0], k))

        print("Pauli IS DONE!")

    split.getData('../data/SAR_data')
    split.getData('../data/Pauli_data')


