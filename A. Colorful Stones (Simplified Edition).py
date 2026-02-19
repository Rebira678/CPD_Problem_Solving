#A. Colorful Stones (Simplified Edition)
#https://codeforces.com/contest/265/problem/A
s=input()
t=input()
string=[]
instruction=[]
for i in s:
    string.append(i)
for i in t:
    instruction.append(i)
    
pointer=0
count=0
for i in range(len(instruction)):
    if instruction[i]==string[pointer]:
        count+=1
        pointer+=1
print(count+1)
