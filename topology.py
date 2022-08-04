# from collections import deque # 큐를 가져옴

# # 노드의 개수와 간선의 개수 입력받기
# v, e = map(int, input().split())

# # 모든 노드에 대한 진입차수는 0으로 초기화
# indegree = [0] * (v+1)

# # 각 노드에 연결된 간선 정보를 담기 위한 연걸 리스트(그래프) 초기화
# graph = [[] for i in range(v + 1)]

# # 방향 그래프의 모든 간선 정보를 입력받기
# for _ in range(e):
#     a, b = map(int, input().split())
#     graph[a].append(b) # 정점 A에서 B로 이동
#     # 진입차수를 1 증가
#     indegree[b] += 1

# # 위상 정렬 함수
# def topology_sort(indegree):
#     result = [] # 알고리즘 수행 결과를 담을 리스트
#     q = deque() # 큐 기능을 위한 deque 라이브러리 사용

#     # 처음 시작할때는 진입차수가 0인 노드를 큐에 삽입
#     for i in range(1, v+1):
#         if indegree[i] == 0:
#             q.append(i)

#     # 큐가 빌 때까지 반복
#     while q:
#         # 큐에서 원소 꺼내기
#         now = q.popleft()
#         result.append(now)

#         # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
#         for i in graph[now]:
#             indegree[i] -= 1
#             # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
#             if indegree[i] == 0:
#                 q.append(i)

#     # 위상 정렬을 수행한 결과 출력
#     for i in result:
#         print(i, end=' ')                

# # 위상 정렬 함수 실행
# topology_sort(indegree)
###################################
# 문제 3
from collections import deque # 큐를 가져옴
import copy

# 노드의 개수 입력받기
v = int(input())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 각 강의를 듣는 시간(비용)을 담을 리스트 추가
cost = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for node in range(v):
    li = list(map(int, input().split()))
    for i in range(len(li) - 1):
        if i == 0:
            cost[node + 1] = li[i] # 비용 입력받기
        else:
            graph[li[i]].append(node + 1) # 정점 li[i]에서 node로 이동
            # 진입차수를 1 증가
            indegree[node + 1] += 1

# 위상 정렬 함수
def topology_sort(indegree, v):
    result = copy.deepcopy(cost) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], (cost[i] + result[now])) # 더 비용이 적은 케이스 계산
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, len(result)):
        print(result[i])                
    

# 위상 정렬 함수 실행
topology_sort(indegree, v)