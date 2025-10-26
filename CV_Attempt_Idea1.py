#The implementation is not fully complete.
#if u want you can look at the code tho :)

import cv2
import numpy as np 
import sys
import itertools
np.set_printoptions(threshold=sys.maxsize)  # command to let me see the full numpy array , not just the edges
#blue_marker = 28
#green marker = 94

img = cv2.imread("maze_image.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#len(gray) -> height
#len(gray[0]) -> width 
img_height = len(gray)
img_width = len(gray[0])
temp = gray[img_height//2]
print(temp)
f=open("data.txt","w")
np.savetxt(f,gray, delimiter=',', fmt='%d')
f.close()
cell_len = []
marker1_loc=[]
marker2_loc=[]
for i in range(len(gray)):
    for j in range(len(gray[0])):
        if(gray[i][j]>25 and gray[i][j] < 35):
            marker1_loc.append([i,j])
        elif(gray[i][j] > 90 and gray[i][j]<100):
            marker2_loc.append([i,j])
m1=[]
m2=[]
sum1 =0;
sum2=0;
for i in marker1_loc:
    sum1+=i[0]
    sum2+=i[1]
m1.append(sum1/len(marker1_loc))
m1.append(sum2/len(marker1_loc))
sum1 =0
sum2=0
for i in marker2_loc:
    sum1+=i[0]
    sum2+=i[1]
m2.append(sum1/len(marker2_loc))
m2.append(sum2/len(marker2_loc))

for i in range(len(gray)):
    for val, grp in itertools.groupby(gray[i]):
        temp_loc = []
        if val == 0 or val == 255:
            width = len(list(grp))
            if(width > 20):
                cell_len.append(width)
            else:
                pass
cell_height = min(cell_len)
for i in range(img_width):
    lst = []
    for j in range(img_height):
        lst.append(gray[j][i])
    for val, grp in itertools.groupby(lst):
        temp_loc = []
        if val == 0 or val == 255:
            width = len(list(grp))
            if(width > 20):
                cell_len.append(width)
            else:
                pass
cell_data = []
node_data = []
cell_width = min(cell_len)
print(m1,m2)
print(cell_height,cell_width)

