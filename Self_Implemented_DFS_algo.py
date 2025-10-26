n = int(input("Enter the number of nodes: "))
data = []
for i in range(n):
    print(f"Enter the adjacent nodes for the {i}th node")
    try:
        data.append(list(map(int,input().split(',')))) #incase u decide to split using ,
    except:
        try:
            data.append(list(map(int,input().split()))) #incase you decide to split using space
        except:
            print("For gods sake , please split the numbers either with , or space")
start = int(input("Enter the starting node : "))
visited = [0]*n
order = [start]
out = []
while(len(order)>0):
    curr_node = order.pop()
    if visited[curr_node] == 0:
        out.append(curr_node)
        visited[curr_node] = 1
        for i in data[curr_node]:
            if visited[i] == 0:
                order.append(i)
print("DFS Order is : \n ",out)