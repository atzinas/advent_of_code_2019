with open("in.txt", "r") as f:
    data_string = f.read().splitlines()
def spl(string):
    return string.split(')') 



def DFS(node, neibours, visited, node_depth):
    result = 0
    if node == 'SAN':
        result = node_depth
    if node not in visited and node in neibours:
        visited.append(node)
        for neibour in neibours[node]:
           result += DFS(neibour, neibours, visited, node_depth + 1)
    return result; 

data_string = list(map(spl, data_string))

neibours = {}

for data in data_string:
    if data[0] not in neibours:
        neibours[data[0]] = [data[1]]
    else:
        neibours[data[0]].append(data[1])  
    if data[1] not in neibours:
        neibours[data[1]] = [data[0]]
    else:
        neibours[data[1]].append(data[0])  
visited = []
depth = DFS('YOU', neibours, visited, 0)

print(depth - 2)
