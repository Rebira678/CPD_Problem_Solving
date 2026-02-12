#https://codeforces.com/contest/677/problem/A
#
n,h =map(int,input().split())
friends=list(map(int,input().split()))
count=0
for i in friends:
    if i>h:
        count+=2
    else:
        count+=1
print(count)
