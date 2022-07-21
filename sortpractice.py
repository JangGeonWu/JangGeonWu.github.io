# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2

#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)

# n = int(input())
# n_li = list(map(int, input().split()))

# n_li.sort()

# m = int(input())
# m_li = list(map(int, input().split()))

# for i in m_li:
#     if binary_search(n_li, i, 0, n - 1) == None: print(0)
#     else: print(1)

##############################################################

n, m = map(int, input().split())

li = list(map(int, input().split()))

li.sort()
mini = 0
maxi = max(li)
while(mini <= maxi):
    mid = (mini + maxi) // 2    
    tot = 0
    for i in li:
        if (i - mid) > 0: tot += (i - mid)       

    if tot < m:
        maxi = mid - 1
    elif tot == m: # 맞추면 루프 탈출
        result = mid
        break
    else:
        result = mid
        mini = mid + 1

print(result)
