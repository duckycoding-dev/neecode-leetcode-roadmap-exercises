# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Constraints:

#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.


#  link: https://leetcode.com/problems/valid-parentheses/description/

from collections import deque

class Solution:
  def isValid(self, s: str) -> bool:
    if(len(s) == 0): return True
    if(len(s) % 2 != 0): return False
    
    parenthesesHashMap = dict({"{":"}", "[":"]", "(":")"})
    stack = deque()
    for c in s:
      if c in parenthesesHashMap.keys():
        stack.append(c)
      elif len(stack) == 0: return False
      else:
        if(c != parenthesesHashMap.get(stack.pop())):
          return False
        
    if(len(stack) == 0): return True
    else: return False


submit = Solution()
print(submit.isValid("()")) # True
print(submit.isValid("()[]{}")) # True
print(submit.isValid("(]")) # False