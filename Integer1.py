nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele % 2 == 1:
        result = result + ele 
print(result)
