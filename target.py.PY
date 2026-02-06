class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
                


nums = list(map(int,input("Enter numbers separated by space").split()))
target = int(input("Enter  a target sum value:"))
solution = Solution()
result = solution.twoSum(nums,target)
print(f"Output:{result}")

        