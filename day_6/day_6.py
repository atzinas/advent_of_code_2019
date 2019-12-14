with open("in.txt", "r") as f:
    data_string = f.read().splitlines()
def spl(string):
    return string.split(')') 

def DFS(node, neibours, visited, node_depth):
    node_sum = node_depth
    if node not in visited and node in neibours:
        visited.add(node)
        for neibour in neibours[node]:
            node_sum += DFS(neibour, neibours, visited, node_depth + 1)
    return node_sum
    

data_string = list(map(spl, data_string))

neibours = {}

for left, right in data_string:
    if left not in neibours:
        neibours[left] = []
    neibours[left].append(right)  
visited = set()
depth = DFS('COM', neibours, visited, 0)

print(depth)
