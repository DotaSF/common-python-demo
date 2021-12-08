import os
 
img_path = 'D:/ball_detect/images'
imglist = os.listdir(img_path)

i = 0
for img in imglist:
    i+=1
    if img.endswith('.jpg'):
        print(i)
        src = os.path.join(os.path.abspath(img_path), img)
        dst = os.path.join(os.path.abspath(img_path), str(i)+'.jpg')
        os.rename(src, dst)