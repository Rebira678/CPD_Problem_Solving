#https://codeforces.com/contest/112/problem/A
#
first=input()
second=input()
first=first.lower()
second=second.lower()
if first<second:
    print(-1)
elif first>second:
    print(1)
else:
    print(0)
