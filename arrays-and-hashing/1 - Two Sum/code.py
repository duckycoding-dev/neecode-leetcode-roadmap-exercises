class Solution:
  def twoSum(self, nums, target):
    mapNums = dict()
    for index, num in enumerate(nums):
      firstValue = mapNums.get(str(target - num))
      if firstValue != None:
        return [firstValue, index]
      else:
        mapNums[str(num)] = index

submit = Solution()
print(submit.twoSum([2, 7, 11, 15], 9))
print(submit.twoSum([3,2,4], 6))
print(submit.twoSum([3,3], 6))
