# two-pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:      
        left, right = 0, len(numbers) - 1
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left + 1, right + 1]
            elif curr < target:
                left += 1
            else:
                right -= 1 

# hashmap
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}

        for i, v in enumerate(numbers):
            if v not in d:
                d[target - v] = i + 1
            else:
                return [d[v], i + 1]
