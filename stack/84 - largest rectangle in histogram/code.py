# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Constraints:

#     1 <= heights.length <= 105
#     0 <= heights[i] <= 104

# link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
  def largestRectangleArea(self, heights: list[int]) -> int:

submit = Solution()
print(submit.largestRectangleArea([2,1,5,6,2,3])) # 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

print(submit.largestRectangleArea([2,4])) # 4