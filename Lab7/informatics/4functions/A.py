def find_min(a,b,c,d):
    mi = 10000
    for i in nums:  
        if(i < mi):
            mi = i
    return mi

nums = list(map(int, input().split()))

print(find_min(nums[0],nums[1],nums[2],nums[3]))

        