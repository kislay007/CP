test=int(input())
l=[]
for i in range(test):
    l.append(int(input()))

last=test
for i in range(test-1, -1, -1):
    if l[i]==last:
        last-=1
print(last)
