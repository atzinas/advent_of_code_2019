with open("in.txt", "r") as f:
    data_string = f.read().splitlines()
def spl(string):
    return string.split(')') 

def DFS(node, neibours, visited, node_depth):
    if node == 'SAN':
        return node_depth
    if node not in visited and node in neibours:
        visited.add(node)
        for neibour in neibours[node]:
            dist = DFS(neibour, neibours, visited, node_depth + 1)
            if dist is not None:
                return dist

data_string = list(map(spl, data_string))

neibours = {}

for left, right in data_string:
    if left not in neibours:
        neibours[left] = []
    neibours[left].append(right)  
    if right not in neibours:
        neibours[right] = []
    neibours[right].append(left)  
visited = set()
depth = DFS('YOU', neibours, visited, 0)

print(depth - 2)
