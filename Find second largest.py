nums = [4,2, 7,7, 83,3]
nums = list(set(nums))

nums.sort()

# nums = sorted(set(nums))
print("second largest:", nums[-2])
print("lowest:", nums[0])