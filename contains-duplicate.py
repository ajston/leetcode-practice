# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

class Solution:
    def ContainsDuplicate(self, nums= [1, 5, 7, 9, 3]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False