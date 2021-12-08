import os
from os import listdir,getcwd

img_path = 'D:/darknet-master/build/darknet/x64/data/obj/'

def getFile_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        print(files)
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.splitext(file)[0]) #L.append(os.path.join(root, file))
    return L

list_file_train = open('D:/darknet-master/build/darknet/x64/data/train.txt','w')
img_ids_train = getFile_name(img_path)
i=0
for img_id in img_ids_train:
    i+=1
    list_file_train.write(img_path + img_id + '.jpg' + '\n')
list_file_train.close()