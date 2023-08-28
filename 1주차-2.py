#백준 28125
n = int(input())
for i in range(n):
    words = list(input())
    cnt = 0
    temp = ''
    j = 0
    while j<len(words):
        if words[j] == '@':
            words[j] = 'a'
            cnt += 1
            temp += 'a'
        elif words[j] == '[':
            words[j] = 'c'
            cnt += 1
            temp+='c'
        elif words[j] == '!':
            words[j] = 'i'
            cnt += 1
            temp+='i'
        elif words[j] == ';':
            words[j] = 'j'
            cnt += 1
            temp+='j'
        elif words[j] == '^':
            words[j] = 'n'
            cnt += 1
            temp+='n'
        elif words[j] == '0':
            words[j] = 'o'
            cnt += 1
            temp+='o'
        elif words[j] == '7':
            words[j] = 't'
            cnt += 1
            temp+='t'
        elif words[j] == '\\':
            cnt += 1
            if words[j + 1] == '\'':
                words[j] = 'v'
                j+=1
                temp+='v'
            else:
                words[j] = 'w'
                j+=2
                temp+='w'
        else:
          temp+=words[j]
        j+=1
    if cnt >= (len(temp)+1) // 2:
        print("I don't understand")
    else:
      print(temp)
#백준 28135
n = int(input())
cnt = 0
for i in range(n):
  if "50" in str(i):
    cnt+=1
  cnt+=1
print(cnt)
#백준 28136
n = input()
arr = list(map(int,input().split()))
cnt = 1
for i in range(len(arr)-1):
  if arr[i] >= arr[i+1]:
    cnt += 1
if arr[0]>arr[-1]:
  cnt -= 1
print(cnt)
#알고리즘 트레이닝 키위주스
def pour(capa, bot, fid, tid):
  for i in range(0,len(fid)):
    f = int(fid[i])
    t = int(tid[i])
    if(int(bot[t]) + int(bot[f]) <= int(capa[t])):
      bot[t] = int(bot[t]) + int(bot[f])
      bot[f] = 0
    else:
      bot[f] = int(bot[f]) - (int(capa[t]) - int(bot[t]))
      bot[t] = int(capa[t])
  return bot

capa = list(input().split())
bot = list(input().split())
fid = list(input().split())
tid = list(input().split())
pour(capa, bot, fid, tid)
