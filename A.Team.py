#https://codeforces.com/contest/231/problem/A
#
n=int(input())
count=0
for _ in range(n):
    people=list(map(int,input().split()))
    if people.count(1)>=2:
        count+=1
print(count)
    
