#https://codeforces.com/contest/791/problem/A
#
limak, Bob = map(int,input().split())
years=0
while limak<=Bob:
    limak*=3
    Bob*=2
    years+=1
print(years)
