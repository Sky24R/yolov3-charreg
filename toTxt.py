import os
import shutil
import random
random.seed(0)
import cv2
import json
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

# sets=[('2012', 'train'), ('2012', 'val'), ('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
# classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
# sets = [('2019', 'train'), ('2019', 'val')]
#
# '''1和l重复, 0和O重复, 此处共列了70个标签'''
# classes = ["plate", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
#            "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L",
#            "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
#            "Y", "Z", "澳", "川", "鄂", "甘", "赣", "港", "贵", "桂",
#            "黑", "沪", "吉", "冀", "津", "晋", "京", "警", "辽", "鲁",
#            "蒙", "闽", "宁", "青", "琼", "陕", "苏", "皖", "湘", "新",
#            "学", "渝", "豫", "粤", "云", "浙", "藏"]
classes = ['truck','plate','car','other']

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)








if __name__ == "__main__":
    json_folder_path = 'D:/dataset/0001/lables/3'  # json文件夹路径
    json_names = os.listdir(json_folder_path)  # file name

    trainval_percent = 0.9
    total_txt = []
    for txt in json_names:
        if txt.endswith(".json"):
            total_txt.append(txt)


    num = len(total_txt)
    list = range(num)
    tv = int(num * trainval_percent)
    trainval = random.sample(list, tv)
    print("train and val size", tv)

    for i in list:
        name = total_txt[i][:-5]
        print("name", name)
        if i in trainval:
            image = cv2.imread("D:/dataset/0001/images/3/" + name + '.jpg')
            size = image.shape
            w = size[1]  # 宽度
            h = size[0]  # 高度

            txt_name = "D:/dataset/0001/lables/labels/train/" + name + '.txt'
            out_file = open(txt_name, 'w')
            json_path = os.path.join(json_folder_path, name+".json")
            print(json_path)
            data = json.load(open(json_path, 'r'))
            labels = data[0]['annotations']

            for i in range(len(labels)):
                lab = labels[i]['label']

                img_w = labels[i]['coordinates']['width']
                img_h = labels[i]['coordinates']['height']

                x = labels[i]['coordinates']['x']
                y = labels[i]['coordinates']['y']

                dw = 1. / w
                dh = 1. / h
                x = x * dw
                img_w = img_w * dw
                y = y * dh
                img_h = img_h * dh
                print(x,y,img_w,img_h)

                for j in range(len(classes)):
                    # if json_name[0:-5] == "1032":
                    #     print("",lab[0:5])
                    if classes[j] == lab[0:5]:

                        out_file.write(str(j)+" "+str(x) + " " + str(y) + " " + str(img_w) + " " + str(img_h))
                    else:
                        continue
                out_file.write("\n")


            shutil.copyfile("D:/dataset/0001/images/3/" + name + '.jpg',
                            "D:/dataset/0001/images/3/train/" + name + '.jpg')

        else:
            image = cv2.imread("D:/dataset/0001/images/3/" + name + '.jpg')
            size = image.shape
            w = size[1]  # 宽度
            h = size[0]  # 高度

            txt_name = "D:/dataset/0001/lables/labels/val/"+ name + '.txt'
            out_file = open(txt_name, 'w')
            json_path = os.path.join(json_folder_path, name + ".json")
            print(json_path)
            data = json.load(open(json_path, 'r'))
            labels = data[0]['annotations']

            for i in range(len(labels)):
                lab = labels[i]['label']

                img_w = labels[i]['coordinates']['width']
                img_h = labels[i]['coordinates']['height']

                x = labels[i]['coordinates']['x']
                y = labels[i]['coordinates']['y']

                dw = 1. / w
                dh = 1. / h
                x = x * dw
                img_w = img_w * dw
                y = y * dh
                img_h = img_h * dh
                print(x, y, img_w, img_h)

                for j in range(len(classes)):
                    # if json_name[0:-5] == "1032":
                    #     print("",lab[0:5])
                    if classes[j] == lab[0:5]:

                        out_file.write(str(j) + " " + str(x) + " " + str(y) + " " + str(img_w) + " " + str(img_h))
                    else:
                        continue
                out_file.write("\n")


            shutil.copyfile("D:/dataset/0001/images/3/" + name + '.jpg',
                            "D:/dataset/0001/images/3/val/" + name + '.jpg')


