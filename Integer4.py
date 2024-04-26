nums = list(map(int, input().split()))
#temp = sum(nums)
sumOfElements = 0 
for ele in nums:
    sumOfElements = sumOfElements + ele 
print(sumOfElements // len(nums))
 
