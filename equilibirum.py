
nums=list(map(int,input().split()))
n=len(nums)
result=-1

for i in range(n):
    leftsum=0
    for j in range(i+1):
        leftsum+=nums[j]
    rightsum=0
    for j in range(i+1,n):
        rightsum+=nums[j]
    if leftsum==rightsum:

        result=i
        break

print(result)        

