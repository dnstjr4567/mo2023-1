
f1 = [ "fis", "gard", "swim", "fis" ]
s1 = [ "hun", "fis", "fis", "bit" ]
f2 = [ "v", "dv", "l", "c" ]
s2 = ["t", "s", "ds", "m" ]
f3 = ["s", "pr", "c", "m" ]
s3 = ["p", "p", "a", "p" ]
f4 = [ "t", "o", "p", "c", "o", "d", "e", "r", "s", "i", "n", "g", "l", "e", "r", "o", "u", "n", "d", "m", "a", "t", "c", "h", "f", "o", "u", "r", "n", "i" ]
s4 = ["n", "e", "f", "o", "u", "r", "j", "a", "n", "u", "a", "r", "y", "t", "w", "e", "n", "t", "y", "t", "w", "o", "s", "a", "t", "u", "r", "d", "a", "y" ]
def best(f,s):
  ans = 0
  for i in range(len(f)):
    ff=0
    ss=0
    for j in range(i,len(f)):
      if f[i]==f[j]:
        ff+=1
      elif f[i] == s[j]:
        ff+=1
      if s[i]==f[j]:
        ss+=1
      if s[i]==s[j]:
        ss+=1
    ans = max(ff,ans)
    ans = max(ss,ans)
  return ans


print(best(f1,s1))
print(best(f2,s2))
print(best(f3,s3))
print(best(f4,s4))
def party(f,s):
  dic = {}
  for i in range(len(f)):
    dic[f[i]]=0
    dic[s[i]]=0
  for i in range(len(f)):
    dic[f[i]]+=1
    dic[s[i]]+=1

  ans = 0
  for i in dic:
    ans = max(ans, dic[i])

  return ans
print(party(f1,s1))
print(party(f2,s2))
print(party(f3,s3))
print(party(f4,s4))
def encrypt(num):
  ans = 1
  num.sort()
  num[0]+=1
  for i in range(len(num)):
    ans *= num[i]
  return ans
n1 = [1, 2, 3 ]
n2 = [ 1, 3, 2, 1, 1, 3 ]
n3 =[1000, 999, 998, 997, 996, 995 ]
n4 = [ 1, 1, 1, 1 ]
print(encrypt(n1))
print(encrypt(n2))
print(encrypt(n3))
print(encrypt(n4))
n1 = [1, 2, 3 ]
n2 = [ 1, 3, 2, 1, 1, 3 ]
n3 =[1000, 999, 998, 997, 996, 995 ]
n4 = [ 1, 1, 1, 1 ]
def encrypt2(num):
  max = 0
  for i in range(len(num)):
    ans = 1
    num[i]+=1
    for j in range(len(num)):
      ans*=num[j]
    num[i]-=1
    if max<ans:
      max = ans
  return max
print(encrypt2(n1))
print(encrypt2(n2))
print(encrypt2(n3))
print(encrypt2(n4))
