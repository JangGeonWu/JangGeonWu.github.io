# # 특정 원소가 속한 집합을 찾기
# def find_parent(parent, x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

# # 두 원소가 속한 집합을 합치기
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# # 노드의 개수와 간선(union 연산)의 개수 입력받기
# v, e = map(int, input().split())
# parent = [0] * (v + 1)

# # 부모 테이블 상에서, 부모를 자기 자신으로 초기화
# for i in range(1, v+1):
#     parent[i] = i

# # union 연산을 각각 수행
# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)

# # 각 원소가 속한 집합 출력
# print('각 원소가 속한 집합: ', end='')
# for i in range(1, v+1):
#     print(find_parent(parent, i), end=' ')

# print()

# # 부모 테이블 내용 출력
# print('부모 테이블: ', end='')
# for i in range(1, v+1):
#     print(parent[i], end=' ')

######## cycle 판별
# 특정 원소가 속한 집합을 찾기, 경로 압축 적용
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# # 두 원소가 속한 집합을 합치기
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# # 노드의 개수와 간선(union 연산)의 개수 입력받기
# v, e = map(int, input().split())
# parent = [0] * (v + 1)

# # 부모 테이블 상에서, 부모를 자기 자신으로 초기화
# for i in range(1, v+1):
#     parent[i] = i

# cycle = False # cycle 발생 여부

# # union 연산을 각각 수행
# for i in range(e):
#     a, b = map(int, input().split())
#     # cycle이 발생하면 바로 종료
#     if find_parent(parent, a) == find_parent(parent, b):
#         cycle = True
#         break
#     else:
#         union_parent(parent, a, b)

# # 사이클 발생 여부 출력
# if cycle:
#     print("cycle occured")
# else:
#     print("cycle didn't occured") 

########################################################
# 문제 1

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 연산의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1)

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

li = [] # 출력용 리스트
# 연산을 각각 수행
for i in range(m):
    k, a, b = map(int, input().split())
    if k == 0: # 합치기 연산이라면
        union_parent(parent, a, b)
    else: # 검색 연산이라면
        if find_parent(parent, a) == find_parent(parent, b): # 같은 팀이면
            li.append('YES')
        else: # 아니면
            li.append('NO')

for i in li:
    print(i)
