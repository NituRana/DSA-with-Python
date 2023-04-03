'''*******************************************************************************************************
Find if an array of strings can be chained to form a circle 

Input: arr[] = {"nitu", "uttarakhan"}
Output: Yes, the given strings can be chained.

Input  : arr[] = ["abc", "efg", "cde", "ghi", "ija"]
Output : Yes

***********************************************************************************************************''' 

def can_form_circle(words):
    # Build the graph
    graph = {}
    in_degree = {}
    out_degree = {}
    for word in words:
        start, end = word[0], word[-1]
        if start not in graph:
            graph[start] = []
            in_degree[start] = 0
            out_degree[start] = 0
        if end not in graph:
            graph[end] = []
            in_degree[end] = 0
            out_degree[end] = 0
        graph[start].append(word)
        in_degree[end] += 1
        out_degree[start] += 1

    # Check if a cycle exists
    stack = [node for node in graph if out_degree[node] == in_degree[node]]
    visited = set(stack)
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            out_degree[node] -= 1
            in_degree[neighbor[0]] -= 1
            if out_degree[node] == in_degree[node]:
                if node not in visited:
                    visited.add(node)
                    stack.append(node)
            elif out_degree[node] < in_degree[node]:
                return False

    return len(visited) == len(graph) and all(deg == 0 for deg in in_degree.values())

words = ['aaa', 'bbb', 'baa', 'aab']
print(can_form_circle(words))  # True

words = ['abc', 'def', 'efg']
print(can_form_circle(words))  # False

