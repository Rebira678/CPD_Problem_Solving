#
#https://codeforces.com/contest/381/problem/A
n=int(input())
points=list(map(int,input().split()))
sereja_point=0
dima_point=0
for i in range(n):
    if i%2==0:
        if points[0]>points[-1]:
            sereja_point+=points[0]
            points.pop(0)
        else:
            sereja_point+=points[-1]
            points.pop()
    else:
        if points[0]>points[-1]:
            dima_point+=points[0]
            points.pop(0)
        else:
            dima_point+=points[-1]
            points.pop()
print(sereja_point,dima_point)
