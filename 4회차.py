#1018
nm = list(map(int,input().split()))
chess = []
for i in range(nm[0]):
  chess.append(input())
min = 9999999
for i in range(nm[0]-7):
  for j in range(nm[1]-7):
    cntb = 0
    cntw = 0
    for t in range(i,i+8):
      for k in range(j,j+8):
        if (t+k)%2 == 0:
          if chess[t][k] == 'B':
            cntw+=1
          else:
            cntb+=1
        else:
          if chess[t][k] == 'W':
            cntw+=1
          else:
            cntb+=1
    if cntw<min:
       min = cntw
    if cntb<min:
      min = cntb
print(min)
#17298
n = int(input())

stack = []
ans = []
nge = list(map(int, input().split()))
stack.append(-1)
stack.append(nge[-1])
ans.append(-1)
for i in range(n-2,-1,-1):
  if(nge[i]>=stack[-1]):
    while stack[-1]!=-1:
      stack.pop()
      if (nge[i]<stack[-1]):
        break
    ans.append(stack[-1])
    stack.append(nge[i])
  else:
      ans.append(stack[-1])
      stack.append(nge[i])

for i in range(n-1,-1,-1):
    print(ans[i], end=' ')
#2217
n = int(input())
ropes = []
for i in range(n):
  ropes.append(int(input()))
ropes.sort()
max = 0
for i in range(n):
  t = ropes[i]*(n-i)
  if(t>max):
    max = t
print(max)
#전체 탐색 중 브루트포스 알고리즘을 공부하고 문제를 해결했다​
  
