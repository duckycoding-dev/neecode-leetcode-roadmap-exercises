# goal: write an algorithm that runs in O(n) time

class Solution:
  def function(self, nums: list) -> int:
    max = 0
    hashMap = dict.fromkeys(nums, 1)
    nums.sort()
    for num in nums:
      previousNumberCount = hashMap.get(num-1)
      if previousNumberCount != None and hashMap.get(num) == 1:
        hashMap[num] = previousNumberCount + 1
      if(hashMap.get(num) > max):
        max = hashMap.get(num)
    return max

submit = Solution()
print(submit.function([100, 4, 200, 1, 3, 2])) # 4
print(submit.function([0,3,7,2,5,8,4,6,0,1])) # 9
print(submit.function([])) # 0
print(submit.function([100])) # 1
print(submit.function([100, 101])) # 2


# approach: divide the problem in subproblems
# from: consecutive sequence starting from nums
# to: consecutive sequence up to n


# base case: 0 items -> 0
# base case: 1 item -> 1
