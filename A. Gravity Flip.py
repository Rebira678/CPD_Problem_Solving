#https://codeforces.com/contest/405/problem/A
#
n=int(input())
content=list(map(int,input().split()))
content.sort()
print(*content)
