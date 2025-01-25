N, M = map(int, input().split())
nums = sorted(set(map(int, input().split())))

def getPermutaion(perm, last):
    if len(perm)==M:
        print(*perm)
        return
    '''
    정렬을했으니 지금 값 인덱스 다음인 애들만 탐색해도 될듯 그럼 굳이 if문 필요 X
    '''
    for i in nums: 
        if last <= i:
            perm.append(i)
            getPermutaion(perm, i)
            perm.pop()

getPermutaion([], 0)