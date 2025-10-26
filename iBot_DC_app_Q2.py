
n = int(input("Enter the value of n of the grid: "))
''' Nodes and their location:
....................... n^2 -1
.
.
2n 2n+1 2n+2
n n+1 n+2................ 2n
0 1 2 3 4 5 6 7 8 9 ... n-1
'''

data = []
data.append([1,n])
for i in range(1,n-1,1):
    data.append([i-1,i+n,i+1])
data.append([n-2,2*n-1])
for i in range(1,n-1,1):
    data.append([i*n+n,i*n+1,i*n-n])
    for j in range(1,n-1,1):
        data.append([i*n+j-1,i*n+j+n,i*n+j+1,i*n+j-n])
    temp = (i+1)*n-1
    data.append([temp-1,temp+n,temp -n])
data.append([n**2-n+1,n**2-2*n])
for i in range(1,n-1,1):
    data.append([n**2-n+i-1,n**2-n+i+1,n**2-n+i-n])
data.append([n**2-2,n**2-n-1])
starting_node = 0
output = []
size= n**2
visited = [0]*(size)
order = [starting_node]
distances = [-1]*size
prev_node = [-1]*size
distances[starting_node]=0


while(len(order)>0):
    current_node = order.pop(0)
    if(visited[current_node] == 0):
        output.append(current_node)
        visited[current_node] = 1
        for i in data[current_node]:
            if visited[i] == 0:
                prev_node[i] = current_node
                distances[i] = distances[current_node]+1
                order.append(i)

reversed_path = []
end_node = n**2-1
reversed_path.append(end_node)
current_node=end_node
while prev_node[current_node]!=-1:
    reversed_path.append(prev_node[current_node])
    current_node =prev_node[current_node]
path = reversed_path[::-1]

print("The BFS Order is: \n",output)
print("Shortest path : \n ",path)