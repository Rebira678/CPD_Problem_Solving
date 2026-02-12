#https://codeforces.com/contest/734/problem/A
#
from collections import Counter
n=int(input())
plays=input()

count=Counter(plays)

if count["A"]>count["D"]:
    print("Anton")
elif count["A"]< count["D"]:
    print("Danik")
else:
    print("Friendship")
