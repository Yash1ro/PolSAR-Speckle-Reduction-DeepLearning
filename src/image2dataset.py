import os
from torchvision import transforms
from PIL import Image
import myLogs as m
from tqdm import tqdm

if not (os.path.exists("../data/train_Pauli")):
    os.mkdir("../data/train_Pauli")
if not (os.path.exists("../data/val_Pauli")):
    os.mkdir("../data/val_Pauli")
if not (os.path.exists("../data/test_Pauli")):
    os.mkdir("../data/test_Pauli")
if not (os.path.exists("../data/Pauli_data")):
    os.mkdir("../data/Pauli_data")




writer = m.Tensorboard().create_board()
# 指定文件路径
root_path = "../data"
target_path = "PauliImage"

# 获取文件列表
img_list = os.listdir(os.path.join(root_path, target_path))

# 创建transform对象
trans_totensor = transforms.ToTensor()
trans_resize = transforms.Resize((1200, 800))
trans_rancrop = transforms.RandomCrop(400)


# 创建数据集
if len(os.listdir("../data/Pauli_data")) == 0:
    for i in tqdm(img_list):
        print(i)
        img = Image.open(os.path.join(root_path, target_path, i))
        print(img)
        img_resized = trans_resize(img)
        print(img_resized)
        img_totensor = trans_totensor(img_resized)

        for k in tqdm(range(1500)):
            img_crop = trans_rancrop(img_totensor)
            toPIL = transforms.ToPILImage()  # 这个函数可以将张量转为PIL图片，由小数转为0-255之间的像素值
            img_dataset = toPIL(img_crop)
            img_dataset.save("../data/Pauli_data/{}_{}.jpg".format(i.split("jpg")[0], k))
            writer.add_image("dataset-{}".format(k), img_crop, k)








