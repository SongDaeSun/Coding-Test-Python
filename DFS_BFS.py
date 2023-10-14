graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False] * 9

dfs(graph, 1, visited)
print()


from collections import deque

def dfs_while(graph, v, visited):
    stack = deque([v])
    
    while stack:
        v = stack.pop()

        if not visited[v]:
            print(v, end=' ')
            visited[v] = True
            stack.extend(graph[v])



visited = [False] * 9

dfs_while(graph, 1, visited)
print()





def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:

        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True




visited = [False] * 9
bfs(graph, 1, visited)
print()
