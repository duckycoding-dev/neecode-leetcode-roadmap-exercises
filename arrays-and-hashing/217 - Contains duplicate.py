class Solution:
  def function(self, nums) -> bool:
    numsMap = set()
    for num in nums:
      if numsMap.__contains__(num):
        return True
      else:
        numsMap.add(num)
    return False

submit = Solution()
res1 = submit.function([1, 2, 3, 1]) # True
res2 = submit.function([1, 2, 3, 4]) # False
res3 = submit.function([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) # True

print(res1, res2, res3)
