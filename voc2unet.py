import os
import random 
random.seed(0)
 
segfilepath=r'./VOCdevkit/VOC2007/SegmentationClass'#标签地址
saveBasePath=r"./VOCdevkit/VOC2007/ImageSets/Segmentation/"#存放txt文件的地址根目录
 
#----------------------------------------------------------------------#
#数据集总数量 = 测试集数量 + （训练集数量 + 验证集数量）
#   想要增加测试集修改trainval_percent
#   修改train_percent用于改变验证集的比例
#----------------------------------------------------------------------#
trainval_percent=1
train_percent=0.9#测试集和验证集9:1

temp_seg = os.listdir(segfilepath)
total_seg = []
for seg in temp_seg:
    if seg.endswith(".png"):
        total_seg.append(seg)#添加标签文件名

num=len(total_seg)#标签数量
list=range(num)  
tv=int(num*trainval_percent)  #训练加验证数量
tr=int(tv*train_percent)  #训练集数量
trainval= random.sample(list,tv)  #随机采样
train=random.sample(trainval,tr)  #随机采样训练集数量
 
print("train and val size",tv)
print("traub suze",tr)
ftrainval = open(os.path.join(saveBasePath,'trainval.txt'), 'w')  #打开根目录下trainval.txt
ftest = open(os.path.join(saveBasePath,'test.txt'), 'w')  #打开test.txt
ftrain = open(os.path.join(saveBasePath,'train.txt'), 'w')  #打开train.txt
fval = open(os.path.join(saveBasePath,'val.txt'), 'w')  #打开val.txt
 
for i  in list:  
    name=total_seg[i][:-4]+'\n'  #每个标签的名称减去末尾四个，即去掉了后缀.png，然后加换行符号
    if i in trainval:  
        ftrainval.write(name)  #训练+验证集
        if i in train:  
            ftrain.write(name)  #训练集
        else:  
            fval.write(name)  #验证集
    else:  
        ftest.write(name)  #剩下的作为测试集
  
ftrainval.close()  
ftrain.close()  
fval.close()  
ftest .close()
