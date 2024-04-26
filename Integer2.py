nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele % 5 == 0:
        result = result + 1 
print(result)
