pre = "pre:"
post = "post:"


def dfs(graph, startnode):
    global pre, post
    visited = [False]*len(graph)  # Flags, welche Knoten bereits besucht wurden
    
    def visit(node):   
        global pre,post           # rekursive Hilfsfunktion, die den gegebenen Knoten und dessen Nachbarn besucht
        if not visited[node]:     # Besuche node, wenn er noch nicht besucht wurde
            visited[node] = True  # Markiere node als besucht
            pre += str(node)+" "            # Ausgabe der Knotennummer - pre-order
            for neighbor in graph[node]:   # Besuche rekursiv die Nachbarn
                visit(neighbor)
            post += str(node)+" "
    visit(startnode)

graph1 = [[1,2],[3,4],[5],[],[],[6], []]
graph2 = [[1,2],[3,4],[7, 5],[],[],[6], [], []]

dfs(graph2, 0)

print(pre)
print(post)