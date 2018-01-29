from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open(r'C:\Users\Administrator\Desktop\Fullmetal_Alchemist_Brotherhood_01v2_[BD_1080p][AtsA][D06FE367].popgo_jp.ass',encoding='UTF-16') as f:
        for line,prevlines in search(f,'Comment',1):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*  20)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

n = fib(10)
for n1 in n:
    print(n1)


q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)

qq = deque(maxlen=3)
qq.append(1)
qq.append(2)
qq.append(3)
qq.appendleft(4)
print(qq)
qq.append(5)
print(qq)