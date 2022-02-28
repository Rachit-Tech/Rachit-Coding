t = int(input())
d = list(map(int, input().split()))
s = sum(d)
d.sort(reverse=True)
count = 0
a = 0
while a<= s//2:
    a+= d[count]

    count+=1
print(count)