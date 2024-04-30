# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Constraints:

#     1 <= temperatures.length <= 105
#     30 <= temperatures[i] <= 100

# link: https://leetcode.com/problems/daily-temperatures/description/

class Solution:
  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

submit = Solution()
print(submit.function([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
print(submit.function([30,40,50,60])) # [1,1,1,0]
print(submit.function([30,60,90])) # [1,1,0]