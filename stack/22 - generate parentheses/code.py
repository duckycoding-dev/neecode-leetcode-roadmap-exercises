# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    # 1 <= n <= 8

# link: https://leetcode.com/problems/generate-parentheses/description/

class Solution:
  def generateParenthesis(self, n: int) -> list[str]:

submit = Solution()
print(submit.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(submit.generateParenthesis(1)) # ["()"]