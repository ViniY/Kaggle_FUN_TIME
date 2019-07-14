import os
import pandas
import PIL
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

width = 300
height = 300

def load_img(path):
    img_dict = {}
    entries = os.listdir(path)
    print(entries)

    img_list = []
    for name in entries:
        address = "E:\Kaggle\\train\\" + name
        # img = cv2.imread(address, 0)

        img = Image.open(address)
        img = img.resize((width, height), Image.LANCZOS)  # best down-sizing filter
        img_list.append(img)
        img_dict[name] = img
        # imgplot = plt.imshow(img)
        # plt.show()
    print("--" * 40)
    print(len(img_dict))

    # basewidth = 300
    # img = Image.open('somepic.jpg')
    # wpercent = (basewidth / float(img.size[0]))
    # hsize = int((float(img.size[1]) * float(wpercent)))
    # img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # use one of these filter options to resize the image
    # im2 = im1.resize((width, height), Image.NEAREST)  # use nearest neighbour
    # im3 = im1.resize((width, height), Image.BILINEAR)  # linear interpolation in a 2x2 environment
    # im4 = im1.resize((width, height), Image.BICUBIC)  # cubic spline interpolation in a 4x4 environment
    # im5 = im1.resize((width, height), Image.ANTIALIAS)  # best down-sizing filter
    return img_dict


def show_image(imgs):
    # img = mpimg.imread('your_image.png')
    imgs_list = list(imgs.values())
    img = imgs_list[5]
    # print(img)
    width = 300
    height = 300
    size = 300, 300
    im5 = img.resize((width, height), Image.LANCZOS)  # best down-sizing filter
    imgplot = plt.imshow(im5, cmap='gray', vmin=0, vmax=255)
    plt.show()
    return


def save_img(img_dict,save_path):
    img_list = list(img_dict.values())
    name_list = list(img_dict.keys())
    for i in range(len(img_list)):
        name = save_path + "//" + name_list[i]
        img_list[i].save(name, "PNG")


def main():

    folder_path_0 = "E:\Kaggle\\test_sampled\\0"
    folder_path_1 = "E:\Kaggle\\test_sampled\\1"
    folder_path_2 = "E:\Kaggle\\test_sampled\\2"
    folder_path_3 = "E:\Kaggle\\test_sampled\\3"
    folder_path_4 = "E:\Kaggle\\test_sampled\\4"

    img_dic_0 = load_img(folder_path_0)
    img_dic_1 = load_img(folder_path_1)
    img_dic_2 = load_img(folder_path_2)
    img_dic_3 = load_img(folder_path_3)
    img_dic_4 = load_img(folder_path_4)

    img_list = list(img_dic_0.values())
    print(np.array(img_list[0].getdata()))
    save_path_0='E:\Kaggle\\test_sampled\downsized\\0'
    save_path_1='E:\Kaggle\\test_sampled\downsized\\1'
    save_path_2='E:\Kaggle\\test_sampled\downsized\\2'
    save_path_3='E:\Kaggle\\test_sampled\downsized\\3'
    save_path_4='E:\Kaggle\\test_sampled\downsized\\4'


    save_img(img_dic_0,save_path_0)
    save_img(img_dic_1,save_path_1)
    save_img(img_dic_2,save_path_2)
    save_img(img_dic_3,save_path_3)
    save_img(img_dic_4,save_path_4)


    # show_image(img_dic)
    return


if __name__ == '__main__':
    main()