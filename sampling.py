import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import keras
import os
import cv2


def read_csv(path):
    df = pd.read_csv(path, sep=",")
    print(df.head())
    print(df.describe())
    print(df.info())
    return df


def read_img(img_folder_path):
    img_dict = {}

    entries = os.listdir(img_folder_path)
    # print(entries)

    img_list = []
    for name in entries:
        address = "E:\Kaggle\\train\\" + name
        img = cv2.imread(address)
        img_list.append(img)
        img_dict[name]=img
    print("//"*40)
    print(len(img_dict))
    # for i in len(img_list):
    return img_dict


# match the image with the label and re-collect & cluster the data
def match_img_with_label(img_dict, df):
    size_class = 100
    df = pd.DataFrame(df)
    id_list = list(df['id_code'])
    label_list = list(df['diagnosis'])
    counter_0 = 0
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    counter_4 = 0
    dict_0 = {}
    dict_1 = {}
    dict_2 = {}
    dict_3 = {}
    dict_4 = {}
    for i in range(len(id_list)):
        name = id_list[i] + ".png"
        # print("+"*80)
        # print(name)
        label = label_list[i]

        if label == 0:
            if counter_0 < size_class:
                counter_0 += 1
                dict_0[name] = img_dict.get(name)

        if label == 1:
            if counter_1 < size_class:
                counter_1 += 1
                dict_1[name] = img_dict.get(name)

        if label == 2:
            if counter_2 < size_class:
                counter_2 += 1
                dict_2[name] = img_dict.get(name)

        if label == 3:
            if counter_3 < size_class:
                counter_3 += 1
                dict_3[name] = img_dict.get(name)

        if label == 4:
            if counter_4 < size_class:
                counter_4 += 1
                dict_4[name] = img_dict.get(name)

    key0 = list(dict_0.keys())
    key1 = list(dict_1.keys())
    key2 = list(dict_2.keys())
    key3 = list(dict_3.keys())
    key4 = list(dict_4.keys())

    img0 = list(dict_0.values())
    img1 = list(dict_1.values())
    img2 = list(dict_2.values())
    img3 = list(dict_3.values())
    img4 = list(dict_4.values())
    print("_"*80)
    print(len(img0))
    folder = "E:\Kaggle\\"

    for i in range(30):
        image_gray_0 = cv2.cvtColor(img0[0-i], cv2.COLOR_BGR2GRAY)
        image_gray_1 = cv2.cvtColor(img1[0-i], cv2.COLOR_BGR2GRAY)
        image_gray_2 = cv2.cvtColor(img2[0-i], cv2.COLOR_BGR2GRAY)
        image_gray_3 = cv2.cvtColor(img3[0-i], cv2.COLOR_BGR2GRAY)
        image_gray_4 = cv2.cvtColor(img4[0-i], cv2.COLOR_BGR2GRAY)
        path0 = folder + "0\\" + key0[0-i]
        path1 = folder + "1\\" + key1[0-i]
        path2 = folder + "2\\" + key2[0-i]
        path3 = folder + "3\\" + key3[0-i]
        path4 = folder + "4\\" + key4[0-i]
        cv2.imwrite(path0, image_gray_0)
        cv2.imwrite(path1, image_gray_1)
        cv2.imwrite(path2, image_gray_2)
        cv2.imwrite(path3, image_gray_3)
        cv2.imwrite(path4, image_gray_4)


def main():
    train_path = "E:\\Kaggle\\train.csv"
    test_path = "E:\\Kaggle\\test.csv"
    img_training_path = "E:\\Kaggle\\train"
    df_train = read_csv(train_path)
    img_dict = read_img(img_training_path)
    match_img_with_label(img_dict, df_train)


if __name__ == '__main__':
    main()
