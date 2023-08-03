#백준 2606
n = int(input())
m = int(input())
computers = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    connect = list(map(int, input().split()))
    computers[connect[0]][connect[1]] = 1
    computers[connect[1]][connect[0]] = 1
visit = [0] * (n + 1)
q = []
q.append(1)
visit[1] = 1
cnt = 0
while q:
  now = q.pop(0)
  for i in range(0,n+1):
    if computers[now][i]==1 and visit[i] == 0:
      q.append(i)
      cnt+=1
      visit[i] = 1
print(cnt)​
#1697
nk = list(input().split())
n = int(nk[0])
k = int(nk[1])
que = []
que.append(n)
dist = [0] * 100001
while len(que)>0:
  now = que.pop(0)
  if now == k:
    print(dist[now])
    break
  for i in range(3):
    if i == 0:
      new = now + 1
      if 0<=new<100001 and dist[new]==0:
        dist[new] = dist[now] + 1
        que.append(new)
    if i == 1:
      new = now - 1
      if 0<=new<100001 and dist[new]==0:
        dist[new] = dist[now] + 1
        que.append(new)
    if i == 2:
      new = now + now
      if 0<=new<100001 and dist[new]==0:
        dist[new] = dist[now] + 1
        que.append(new)
#7576
import sys

input = sys.stdin.readline

mn = list(map(int,input().split()))
box = [[0 for col in range(mn[0])] for row in range(mn[1])]
day =  [[0 for col in range(mn[0])] for row in range(mn[1])]
que = []
for i in range(mn[1]):
  to = list(map(int,input().split()))
  for j in range(mn[0]):
    box[i][j] = to[j]
    if to[j]==1:
      que.append((i,j))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
while len(que)>0:
  x,y = que.pop(0)
  for i in range(4):
    nx = x +dx[i]
    ny = y+dy[i]
    if 0<=nx<mn[1] and 0<=ny<mn[0] and box[nx][ny]==0:
      box[nx][ny] = 1
      day[nx][ny] = day[x][y]+1
      que.append((nx,ny))
max = -1
err = 0
for i in range(mn[1]):
  for j in range(mn[0]):
    if box[i][j] == 0:
      err = -1
      break
    if max < day[i][j]:
      max = day[i][j]
if err == -1:
  print(-1)
else:
  print(max)
#7562
tc = int(input())
dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]
while tc>0:
  idx = int(input())
  matrix = [[0 for col in range(idx)] for row in range(idx)]
  que = []
  now = list(map(int, input().split()))
  target = list(map(int, input().split()))
  que.append(now)
  while len(que)>0:
    x,y = que.pop(0)
    if x == target[0] and y == target[1]:
      print(matrix[x][y])
      break
    for j in range(len(dx)):
      newx = x + dx[j]
      newy = y + dy[j]
      if 0<=newx<idx and 0<=newy<idx and matrix[newx][newy]==0:
        que.append([newx,newy])
        matrix[newx][newy] = matrix[x][y] + 1
  tc-=1
  #bfs dfs에대한 ​ 공부후 문제 해결
