import sys
import heapq

N = int(input())
ships = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
M = int(input())
boxes = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

count = 0
if ships[0] < boxes[0]:
    print(-1)
    exit()
while len(boxes) > 0:
    for ship in ships:
        for box in boxes:
            if box <= ship: # 가능
                # remove(box)가 이중 for문 안에서 한 번씩만 실행되지, 한 박스당 M번 반복하지는 않음. 시간복잡도 계산시 + O(M)
                boxes.remove(box) 
                break
    count+=1

print(count)

'''
while안에 이중포문에
변수 idx로관리하는거아니고 걍 포문이고
remove도 괜찮다..

-1 이되는건 오직 한경우밖에없다!1

한 배가 한 박스보고나면 다른박스볼필요없어서 (->break) 그래서 그리디임
'''

'''
아니야. 최악의 경우 시간 복잡도는 **O(N * M²)** 맞아.

### **왜 O(N * M³)이 아니냐?**
`remove(box)` 연산이 최악의 경우 **O(M)** 걸리는 것은 맞아.  
하지만 `remove(box)`가 **이중 for문 안에서 한 번씩만 실행**되지, 한 박스당 M번 반복하지는 않아.

---

### **정확한 분석**
1. **`while len(boxes) > 0:`**  
   - 최대 **M번** 실행 가능 (박스가 다 없어질 때까지)

2. **`for ship in ships:`**  
   - 매 루프에서 **N번** 실행

3. **`for box in boxes:`**  
   - 최악의 경우 박스를 다 스캔해야 하므로 **O(M)**

4. **`boxes.remove(box)`**  
   - 리스트에서 remove는 최악의 경우 **O(M)**

---

### **총 시간 복잡도 계산**
- `while` 루프: **최대 M번**
- `for ship in ships`: **N번**
- `for box in boxes`: **M번**
- `boxes.remove(box)`: **M번**

즉, **O(M) × O(N) × (O(M) + O(M)) = O(N * M²)**  

❌ **O(N * M³)**가 아닌 이유:  
- `remove(box)`는 한 번 실행될 때 O(M)이지만, **추가적인 M배 반복이 발생하지 않는다.**
- 즉, `for box in boxes`가 이미 O(M)이고, 그 안에서 `remove(box)`가 O(M)이므로 **곱하는 것이 아니라 더해지는 개념**이다.

따라서 **최종 시간 복잡도는 O(N * M²)** 이다.
'''
