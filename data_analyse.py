import matplotlib.pyplot as plt
import numpy as np
import os.path as osp
import os
from matplotlib.pyplot import MultipleLocator#设置刻度标签

with open('./dataset/et_71.txt','r',encoding='utf-8') as l:#打开数据名称文件.txt，命名形式一致 img_白菜_62.jpeg, 11 img_白菜_63.jpeg, 11
    data=l.readlines()#读入数据

y_data=[0]*43#43个类，类别数
x_data=[i for i in range(43)]
for d in data:#每行字符串
    y_data[int(d.split(',')[1].split('\n')[0])]+=1#首先进行逗号分割，取第二段；再进行换行键，取第一段；即提取出来的是类别对应的数字。对ydata寻址之后+1，即计数
# 构建数据
# x_data=sorted([int(key) for key in dataset.keys()])
# y_data =[dataset[str(i)] for i in x_data]
num = np.sum(np.array(y_data))#总数量
#
#
print(x_data,y_data)




plt.figure(figsize = (30,24))#figsize:指定figure的宽和高，单位为英寸；
#
plt.bar(left=x_data, height=y_data, width=0.9,label='total nums %s'%(str(num)),color='steelblue', alpha=0.8)#竖值条形图
"""
x	x坐标	int,float
height	条形的高度	int,float
width	宽度	0~1，默认0.8
botton	条形的起始位置	也是y轴的起始坐标
align	条形的中心位置	“center”,"lege"边缘
color	条形的颜色	“r","b","g","#123465"，默认“b"
edgecolor	边框的颜色	同上
linewidth	边框的宽度	像素，默认无，int
tick_label	下标的标签	可以是元组类型的字符组合
log	y轴使用科学计算法表示	bool
orientation	是竖直条还是水平条	竖直："vertical"，水平条："horizontal"
"""
#
for x, y in enumerate(y_data):#同时遍历数据和数据下标
    plt.text(x, y, '%s' % y, ha='center', va='bottom',fontsize=20)#在柱状条上面显示文本；va垂直对齐方式，ha水平对齐方式
    # plt.text(x, y, '%s' % x, ha='center', va='top',fontsize=20)

plt.xticks([index  for index in x_data], x_data)#显示x轴刻度


plt.title('The distribution of all dataset',fontsize=20)#数据集分布

plt.xlabel('labels',fontsize=20)
plt.ylabel("numbers",fontsize=20)

plt.legend()#加上图例
plt.savefig('All-data.png')
plt.show()