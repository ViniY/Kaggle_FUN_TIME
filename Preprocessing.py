import os
import pandas
import PIL
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def load_img(path):
    img_dict = {}
    entries = os.listdir(path)
    print(entries)

    img_list = []
    for name in entries:
        address = "E:\Kaggle\\train\\" + name
        img = cv2.imread(address, 0)
        img_list.append(img)
        img_dict[name] = img
    print("--" * 40)
    print(len(img_dict))
    return img_dict


def show_image(imgs):
    # img = mpimg.imread('your_image.png')
    imgs_list = list(imgs.values())
    img = imgs_list[5]
    # print(img)
    imgplot = plt.imshow(img ,cmap='gray', vmin=0, vmax=255)
    plt.show()
    return


def main():
    folder_path = "E:\Kaggle\\4"
    img_dic = load_img(folder_path)
    show_image(img_dic)
    return


if __name__ == '__main__':
    main()