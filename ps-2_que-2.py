class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def make_graph(numTasks, prerequisites):
    graph = []
    for i in range(numTasks):
        graph.append([])

    for pre in prerequisites:
        graph[pre.second].append(pre.first)

    return graph

def dfs_cycle(graph, node, onpath, visited):
    if visited[node]:
        return False
    onpath[node] = visited[node] = True
    for neigh in graph[node]:
        if onpath[neigh] or dfs_cycle(graph, neigh, onpath, visited):
            return True
    onpath[node] = False
    return False

def canFinish(numTasks, prerequisites):
    graph = make_graph(numTasks, prerequisites)
    onpath = [False] * numTasks
    visited = [False] * numTasks
    for i in range(numTasks):
        if not visited[i] and dfs_cycle(graph, i, onpath, visited):
            return False
    return True

def main():
    numTasks = int(input("Enter the number of tasks: "))
    
    prerequisites = []
    while True:
        try:
            v1, v2 = map(int, input("Enter prerequisite (first second), or Enter to execute: ").split())
            prerequisites.append(Pair(v1, v2))
        except ValueError:
            break
    
    if canFinish(numTasks, prerequisites):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
