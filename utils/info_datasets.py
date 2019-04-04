import os
import argparse
import math
parser   = argparse.ArgumentParser()
parser.add_argument('-dataset_name', type=str, default='',help='') #TT100K_detection, Udacity

if __name__ == "__main__":
    FLAGS, unparsed = parser.parse_known_args()
    dataset = FLAGS.dataset_name
    path = "/home/mcv/datasets/M5/detection/"+dataset
    path_to_save = "/home/grupo07/M5/yolov3/dataset_info"
    arr = os.listdir(path)

    for folder in arr:
        if os.path.isdir(os.path.join(path, folder)):
            if folder == "train":
                dir_images = []
                for image in os.listdir(os.path.join(path,folder)):
                    if "txt" not in image:
                        dir_images.append(image)
                with open(path_to_save + "/" + dataset + "_" + folder + ".txt", 'w') as f:
                    for item in dir_images:
                        f.write("%s\n" % (path + "/" + folder + "/" + item))
            if folder == "test":
                dir_images = []
                for image in os.listdir(os.path.join(path,folder)):
                    if "txt" not in image:
                        dir_images.append(image)
                with open(path_to_save + "/" + dataset + "_" + folder + ".txt", 'w') as f:
                    for item in dir_images:
                        f.write("%s\n" % (path + "/" + folder + "/" + item))
            if folder == "valid":
                dir_images = []
                for image in os.listdir(os.path.join(path,folder)):
                    if "txt" not in image:
                        dir_images.append(image)
                with open(path_to_save + "/" + dataset + "_" + folder + ".txt", 'w') as f:
                    for item in dir_images:
                        f.write("%s\n" % (path + "/" + folder + "/" + item))

