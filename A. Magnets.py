#https://codeforces.com/contest/344/problem/A
#
t=int(input())
magnets=[]
for _ in range(t):
    one=input()
    magnets.append(one)
count=0
for i in range(t-1):
    if magnets[i]!=magnets[i+1]:
        count+=1
print(count+1)
