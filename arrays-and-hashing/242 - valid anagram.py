# goal:

class Solution:
  def isAnagram(self, s, t):
    lettersCount = dict()
    if(len(t) != len(s)):
      return False
    for letter in s:
      if (letter in lettersCount):
        lettersCount[letter] += 1
      else:
        lettersCount[letter] = 1
    for letter in t:
      if (letter in lettersCount):
        if lettersCount[letter] == 0:
          return False
        lettersCount[letter] -= 1
      else:
        return False
    return True

submit = Solution()
print(submit.validAnagram("anagram", "nagaram")) # True
print(submit.validAnagram("rat", "car")) # False