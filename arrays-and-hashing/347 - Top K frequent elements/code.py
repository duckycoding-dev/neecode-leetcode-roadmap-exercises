# goal:

def getMax(d: dict):
  max = None
  for key in d:
    if max == None:
      max = key
      continue
    else:
      if d.get(key) > d.get(max):
        max = key
  return max

class Solution:
  def topKFrequent(self, nums: list[int], k = 0):
    hash = dict()
    res = [k]*(0)
    for n in nums:
      if n in hash:
        hash[n] += 1
      else:
        hash[n] = 1
    for _ in range(k):
      if(len(hash) > 0):
        max = getMax(hash)
        res.append(max)
        hash.__delitem__(max)
    return res
  
submit = Solution()
print(submit.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(submit.topKFrequent([1], 1)) # [1]
print(submit.topKFrequent([], 1)) # []

# TODO: Better solution