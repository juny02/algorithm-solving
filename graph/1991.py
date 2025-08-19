import sys
sys.setrecursionlimit(10**6)

N = int(input())
tree = {}
for _ in range(N):
    a, b, c = input().split()
    tree[a] = [b, c]

def preorder(tree, v, visited):
    print(v, end='')
    
    for n in tree[v]:
        if n!="." and n not in visited:
            visited.add(n)
            preorder(tree, n, visited)

def inorder(tree, v, visited):
    a, b = tree[v]
    if a!="." and a not in visited:
        visited.add(a)
        inorder(tree, a, visited)
    print(v, end='')
    visited.add(v)
    if b!="." and b not in visited:
        visited.add(b)
        inorder(tree, b, visited)

def postorder(tree, v, visited):
    a, b = tree[v]
    if a!="." and a not in visited:
        visited.add(a)
        postorder(tree, a, visited)
    if b!="." and b not in visited:
        visited.add(b)
        postorder(tree, b, visited)
    print(v, end='')
    visited.add(v)

preorder(tree, "A", set())
print()
inorder(tree, "A", set())
print()
postorder(tree, "A", set())
print()