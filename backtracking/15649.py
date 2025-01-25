N, M = map(int, input().split())

def getPermutaion(perm):
    if len(perm) == M:
        print(*perm)
        return
    
    for i in range(1, N+1):
        perm.append(i)
        getPermutaion(perm)
        perm.pop()

getPermutaion([])