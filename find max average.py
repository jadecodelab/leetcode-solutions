
# You are given an integer array nums consisting of n elements,
# and an integer k. Find a contiguous subarray whose length is
# equal to k that has the maximum average value and return this value

def max_average(nums,k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    max_total = curr
    for i in range(k,len(nums)):
        curr += nums[i]-nums[i-k]
        max_total = max(max_total,curr)
    return float(max_total/k)


# test
nums = [1,12,-5,-6,50,3]
k = 4
print(max_average(nums,k))

# O(n) time, O(1) space
