# d = [0] * 100 # 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x] # 이미 계산한 적 있는 문제라면 그대로 반환
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# print(fibo(99)) 

# def fibo(x):
#     print('f(' + str(x) + ')', end=' ')
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x-1) + fibo(x-2)

# print(fibo(10))    

# d = [0] * 100 # 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화

# def fibo(x):
#     print('f(' + str(x) + ')', end=' ')
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x] # 이미 계산한 적 있는 문제라면 그대로 반환
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# print(fibo(10)) 

# d = [0] * 100

# d[1], d[2] = 1, 1
# n = 10

# for i in range(3, n + 1):
#     print('d['+ str(i)+ ']', end=' ')
#     d[i] = d[i - 1] + d[i - 2]

# print(d[n])

# x = int(input())

# d = [0] * 1000001

# for i in range(2, x+1):
#     d[i] = d[i - 1] + 1
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3] + 1)
        
# print(d[x])  

# x = int(input())

# k = list(map(int, input().split()))

# d = [0] * (len(k))

# for i in range(len(k)):
#     if i <= 1:
#         d[i] = k[i]
#     else:
#         d[i] = max(d[:i-1]) + k[i]

# print(d[x-1])        
# n = int(input())
# if n % 2 == 1: print(0)

# else:
#     n = n // 2
#     d = [0] * (n + 1)
#     d[0] = 1
#     d[1] = 3   
    
#     if n > 1:
#         for i in range(2, n+1):
#             d[i] = (d[i-1] * 3) + (sum(d[:i-1]) * 2)
    
#     print(d[n])


n, m = map(int, input().split())

li = []

it = [100] * (m+1)

for _ in range(n):
    li.append(int(input()))


def dp(num, iterate):
    if num > m:
        pass

    for i in li:
        if num + i <= m:
            it[num + i] = min(it[num + i], iterate + 1)
            dp(num + i, iterate + 1)

dp(0, 0)  
if it[m] == 100: print(-1)
else: print(it[m])
