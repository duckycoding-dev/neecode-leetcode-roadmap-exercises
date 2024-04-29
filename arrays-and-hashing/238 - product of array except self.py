# goal: write an algorithm that runs in O(n) time, without using the division operation

class Solution:
  def bruteForce(self, nums: list[int]) -> list[int]: # O(n^2)
    hashMap = dict()
    answer: list = [1]*len(nums)
    for index, num in enumerate(nums):
      if num in hashMap:
        answer[index] = hashMap.get(num)
      else:
        productOfAllExceptNum = 1
        for index2, num2 in enumerate(nums):
          if index2 != index:
            productOfAllExceptNum *= num2
        answer[index] = productOfAllExceptNum
        hashMap[num] = productOfAllExceptNum

    return answer
  
  def productExceptSelf(self, nums: list[int]) -> list[int]: 
    # time complexity = O(n) + O(n) = O(2n) = O(n)
    # extra space complexity = O(n) + O(n) = O(2n) = O(n) (because of the two extra array)
    answer: list = [1]*len(nums)
    hashProductLeft = dict()
    hashProductRight = dict()
    for i in range(len(nums)):  # O(n)
      hashProductLeft[-1] = 1
      hashProductRight[len(nums)] = 1
      if i == 0:
        hashProductLeft[i] = 1
        hashProductRight[len(nums) - 1] = 1
      else:
        hashProductLeft[i] = hashProductLeft.get(i-1) * nums[i-1]
        hashProductRight[len(nums) - 1 - i] = nums[len(nums) - 1 - i + 1] * hashProductRight.get(len(nums) - 1 - i + 1)
    for i in range(len(nums)):  # O(n)
      answer[i] = hashProductLeft.get(i) * hashProductRight.get(i)

    return answer


  def productExceptSelfOptimal(self, nums: list[int]) -> list[int]:
    arr = [1] * (len(nums))
    pre_product = 1
    for i in range(len(nums)):
      arr[i] *= pre_product
      pre_product *= nums[i]
    
    post_product = 1
    for i in range(len(nums)-1, -1, -1):
      arr[i] *= post_product
      post_product *= nums[i]

    return arr

submit = Solution()
print(submit.bruteForce([1,2,3,4])) # [24,12,8,6]
print(submit.bruteForce([-1,1,0,-3,3])) # [0,0,9,0,0]
print(submit.bruteForce([0,0])) # [0,0]
print(submit.productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(submit.productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]
print(submit.productExceptSelf([0,0])) # [0,0]

# approach: save the products of all the values before and after a given one using a hashMap
# things I didn't think about: store pre and post products directly in the array, one of the two first