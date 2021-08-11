def max_num(nums):
      max_number = nums[0]

      for num in nums:
            if num > max_number:
                  max_number = num
      return max_number

print(max_num([50, -10, 0, 75, 20, 100]))