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
  
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    res: list[list] = []
    for string in strs:
      added = False
      for index in range(len(res)):
        if(not added):
          if self.isAnagram(res[index][0], string):
            res[index].append(string)
            added = True
      if(not added):
        res.append([string])
    return res
  
submit = Solution()
print(submit.groupAnagrams(["eat", "eat", "tea", "tan", "ate", "nat", "bat"])) # [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
print(submit.groupAnagrams([""])) # [[""]]
print(submit.groupAnagrams(["a"])) # [["a"]]

# TODO: Better solution