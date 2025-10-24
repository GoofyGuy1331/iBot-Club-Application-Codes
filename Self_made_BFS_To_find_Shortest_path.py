#this is a contd of the Self_implemented_BFS_Algo
#the input format is basically for each node, enter the nodes adjacent to it.
#id suggest to create an input file and do : python3 {saved_file_name}.py < {inputfilename}.txt
#eg inputfile:

#Source used to understand the algo: https://www.geeksforgeeks.org/dsa/shortest-path-unweighted-graph/

''' input_file_example.txt : 
7
1,2
1,3,4
0,4,5
1,6
1,2
2
3
0
5
'''
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
distances = [-1]*n
prev_node = [-1]*n
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
end_node = int(input("Enter the ending node: "))
reversed_path.append(end_node)
current_node=end_node
while prev_node[current_node]!=-1:
    reversed_path.append(prev_node[current_node])
    current_node =prev_node[current_node]
path = reversed_path[::-1]

print("The BFS Order is: \n",output)
print("Shortest path : \n ",path)