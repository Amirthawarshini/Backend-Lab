def find_missing(nums):
    n = len(nums) + 1
    return n * (n + 1) // 2 - sum(nums)

print(find_missing([1, 2, 4, 5, 6]))  