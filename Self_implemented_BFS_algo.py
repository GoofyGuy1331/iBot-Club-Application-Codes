#imma follow same format as the geeks for geeks ppl for input
#learnt how BFS works from : https://www.youtube.com/watch?v=xlVX7dXLS64
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
starting_node = int(input("Enter the node to start from : "))
output = []
visited = [0]*n
order = [starting_node]
print("The BFS Order is: ")
while(len(order)>0):
    current_node = order.pop(0)
    if(visited[current_node] == 0):
        output.append(current_node)
        visited[current_node] = 1
        for i in data[current_node]:
            if visited[i] == 0:
                order.append(i)
print(output)

