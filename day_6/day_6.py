with open("in.txt", "r") as f:
    data_string = f.read().splitlines()
def spl(string):
    return string.split(')') 



def DFS(node, neibours, visited, node_depth):
    node_sum = node_depth
    if node not in visited and node in neibours:
        visited.append(node)
        for neibour in neibours[node]:
            node_sum += DFS(neibour, neibours, visited, node_depth + 1)
    return node_sum
    

data_string = list(map(spl, data_string))

neibours = {}

for data in data_string:
    if data[0] not in neibours:
        neibours[data[0]] = [data[1]]
    else:
        neibours[data[0]].append(data[1])  
visited = []
depth = DFS('COM', neibours, visited, 0)

print(depth)
