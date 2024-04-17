g=[1,10,3,5,7,6,9,120]
length=len(g)
result=g[0]
for i in range(length):
    if g[i]<result:
        result=g[i]
print (result)             
# print(n)
l=list(map(int,input().split()))
print(l)
w=set(l)
print(w)
print(l[-1])

word=input()
print(word[5:9])
print(word[14:21])
print(word[21:25])
print(word[0:4])
print(word[5:16])
print(word[17:30])
print(word[20:13:-1])
print(word[-7:-14:-1])
