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

    writer = m.Tensorboard().create_board()
    # 指定文件路径
    root_path = "../data"
    target_path_1 = "SARImage"
    target_path_2 = "PauliImage"

    # 获取文件列表
    img_list_1 = os.listdir(os.path.join(root_path, target_path_1))
    img_list_2 = os.listdir(os.path.join(root_path, target_path_2))

    # 创建transform对象
    trans_totensor = transforms.ToTensor()
    trans_resize = transforms.Resize((800, 1200))
    trans_rancrop = transforms.RandomCrop(600)
    # trans_normal = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])


    # 创建数据集
    if len(os.listdir("../data/SAR_data")) == 0:
        for i in tqdm(img_list_1):
            print(i)
            img = Image.open(os.path.join(root_path, target_path_1, i))
            print(img)
            img_resized = trans_resize(img)
            print(img_resized)
            img_totensor = trans_totensor(img_resized)
            # img_normal = trans_normal(img_totensor)

            for k in tqdm(range(1000)):
                img_crop = trans_rancrop(img_totensor)
                toPIL = transforms.ToPILImage()  # 这个函数可以将张量转为PIL图片，由小数转为0-255之间的像素值
                img_dataset = toPIL(img_crop)
                img_dataset.save("../data/SAR_data/{}_{}.png".format(i.split(".png")[0], k))
                writer.add_image("dataset-{}".format(k), img_crop, k)

        print("SAR IS DONE!")


    if len(os.listdir("../data/Pauli_data")) == 0:
        for i in tqdm(img_list_2):
            print(i)
            img = Image.open(os.path.join(root_path, target_path_2, i))
            print(img)
            img_resized = trans_resize(img)
            print(img_resized)
            img_totensor = trans_totensor(img_resized)
            # img_normal = trans_normal(img_totensor)

            for k in tqdm(range(1000)):
                img_crop = trans_rancrop(img_totensor)
                toPIL = transforms.ToPILImage()  # 这个函数可以将张量转为PIL图片，由小数转为0-255之间的像素值
                img_dataset = toPIL(img_crop)
                writer.add_image("dataset", trans_totensor(img_dataset), k)
                img_dataset.save("../data/Pauli_data/{}_{}.png".format(i.split(".png")[0], k))
                writer.add_image("dataset-{}".format(k), img_crop, k)

        print("Pauli IS DONE!")

    split.getData('../data/SAR_data')
    split.getData('../data/Pauli_data')
    writer.close()


