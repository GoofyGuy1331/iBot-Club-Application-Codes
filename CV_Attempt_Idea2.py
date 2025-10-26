import cv2
import numpy as np 
import sys
import itertools
np.set_printoptions(threshold=sys.maxsize)  # command to let me see the full numpy array , not just the edges
#blue_marker = 28
#green marker = 94

def check_nearest_white(i ,j,num):
    for x in range(num):
        if(gray[i+x][j] == 255 and i+x>0 and j>0):
            return [i+x,j]
        elif(gray[i-x][j] == 255 and i-x>0 and j>0):
            return [i-x,j]
        elif(gray[i][j+x] == 255 and i>0 and j+x>0):
            return [i,j+x]
        elif(gray[i][j-x]==255 and i>0 and j-x>0):
            return [i,j-x]
    return -1

def checknearby(i,j,num):
    damn =1
    for x in range(-5,6,1):
        for y in range(-5,6,1):
            if(gray[i+x][j+y]==num):
                pass
            else:
                damn = 0
    if(damn):
        return True
    else:
        return False

img = cv2.imread("maze_image.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#len(gray) -> height
#len(gray[0]) -> width 
img_height = len(gray)
img_width = len(gray[0])

bigger_num = 0
iorj = -1
if(img_width>img_height):
    bigger_num = img_width
    iorj = 0
else:
    bigger_num = img_height
    iorj= 1
found_start = 1
found_end = 1
start_node = -1
end_node = -1
temp = []
done1 = 0
done2 = 0
for i in range(img_height):
    for j in range(img_width):
        if(found_start):
            if gray[i][j] == 28 and checknearby(i,j,28) and i > 50 and j > 50 and i <(img_height-10) and j<(img_width-10):    
                print(i,j)
                x,y = check_nearest_white(i,j,50)
                print(x,y)
                if(iorj == 0):
                    start_node = y*bigger_num+x
                else:
                    start_node = x*bigger_num+y
                done1 = 1
                found_start =0
                

        if(found_end):
            if gray[i][j] == 94 and checknearby(i,j,94) and i > 50 and j > 50 and i <(img_height-10) and j<(img_width-10):      
                print(i,j)
                x,y = check_nearest_white(i,j,50)
                print(x,y)
                if(iorj == 0):
                    end_node = y*bigger_num+x
                else:
                    end_node = x*bigger_num+y
                done2 = 1
                found_end = 0
        if(done1 == 1 and done2 == 1):
            break        
    if(done1 == 1 and done2 == 1):
        break    
        
def node_num(i,j):
    if(iorj==0):
        return j*bigger_num+i
    else:
        return i*bigger_num+j
node_adjacents = [[]]*bigger_num*bigger_num
for i in range(img_height):
    for j in range(img_width):
        temp = []
        if((gray[i][j] > 240 or (gray[i][j]>25 and gray[i][j] <35 )or (gray[i][j] > 90 and gray[i][j] < 100)) and i <(img_height-1) and j<(img_width-1)):
            if(((gray[i-1][j] > 240) or (gray[i-1][j]>25 and gray[i-1][j] <35 )or (gray[i-1][j] > 90 and gray[i-1][j] < 100))and i <(img_height-1) and j<(img_width-1)):
                temp.append(node_num(i-1,j))
            if(((gray[i][j+1] > 240) or (gray[i][j+1]>25 and gray[i][j+1] <35 )or (gray[i][j+1] > 90 and gray[i][j+1] < 100)) and i <(img_height-1) and j<(img_width-1)):
                temp.append(node_num(i,j+1))
            if(((gray[i+1][j] > 240) or (gray[i+1][j]>25 and gray[i+1][j] <35 )or (gray[i+1][j] > 90 and gray[i+1][j] < 100)) and i <(img_height-1) and j<(img_width-1)):
                temp.append(node_num(i+1,j))
            if(((gray[i][j-1] > 240)  or (gray[i][j-1]>25 and gray[i][j-1] <35 )or (gray[i][j-1] > 90 and gray[i][j-1] < 100)) and i <(img_height-1) and j<(img_width-1)):
                temp.append(node_num(i,j-1))
        if(temp != []):
            node_adjacents[node_num(i,j)] = temp
starting_node = start_node
output = []
visited = []
order = [starting_node]
distances = [-1]*bigger_num*bigger_num
prev_node = []
distances[starting_node]=0
data = node_adjacents

while(len(order)>0):
    current_node = order.pop(0)
    if(current_node not in visited):
        output.append(current_node)
        visited.append(current_node)
        for i in data[current_node]:
            if i not in visited:
                prev_node.append([current_node,i])
                distances[i] = distances[current_node]+1
                order.append(i)
reversed_path = []
end_node = end_node
reversed_path.append(end_node)
current_node=end_node


f=open("data2.txt","w")
f.write(str(prev_node))
f.close()

while current_node!= start_node:
    for i in range(len(prev_node)):
        if(prev_node[i][1] == current_node):
            num = i
            break
    reversed_path.append(prev_node[num][0])
    current_node = prev_node[num][0]
path = reversed_path[::-1]
print(path)