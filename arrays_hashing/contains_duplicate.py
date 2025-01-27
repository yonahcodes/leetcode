"""
LeetCode 217 - Contains Duplicate

Description :
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    Example 1:
        Input: nums = [1,2,3,1]
        Output: true
        Explanation: The element 1 occurs at the indices 0 and 3.

    Example 2:
        Input: nums = [1,2,3,4]
        Output: false
        Explanation: All elements are distinct.

    Example 3:
        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true

Last Update : 2025-01-27
"""


# Brute force approach:
# Time complexity: O(n^2) - Uses two nested loops. Outer loop runs n times, inner loop runs n - i - 1 times.
# Memory complexity: O(1) - Does not use any additional data structures.
# Where n is the size of nums.
class SolutionBruteForce:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Loop through each element in the array
        for i in range(len(nums)):
            # Compare the current element with the subsequent elements
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:  # Check if elements are identical
                    return True  # Duplicate found
        return False  # No duplicates found


# Sorting approach:
# Time complexity: O(n log n) - Sorting the array dominates the complexity.
# Memory complexity: O(1) - Sorting is performed in place and does not use extra memory.
# Where n is the size of nums.
class SolutionSorting:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Sort the array in place
        nums.sort()
        # Check adjacent elements for duplicates
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:  # Check if adjacent elements are identical
                return True  # Duplicate found
        return False  # No duplicates found


# Set approach:
# Time complexity: O(n) - Adding elements to a set and checking membership is O(1) on average, repeated n times.
# Memory complexity: O(n) - A set is used to store up to n elements in the worst case.
# Where n is the size of nums.
class SolutionSet:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Use a set to store seen elements
        hashset = set()
        for num in nums:
            if num in hashset:  # Check if the number is already in the set
                return True  # Duplicate found
            hashset.add(num)  # Add the number to the set
        return False  # No duplicates found


# Brute force approach
print("-" * 54)
print("Brute Force Approach Results:")
print("-" * 54)
print(f"Input: [1, 2, 3, 1] => Output: {SolutionBruteForce().containsDuplicate([1, 2, 3, 1])}")
print(f"Input: [1, 2, 3, 4] => Output: {SolutionBruteForce().containsDuplicate([1, 2, 3, 4])}")
print(f"Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] => Output: {SolutionBruteForce().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])}")
print()

# Sorting approach
print("-" * 54)
print("Sorting Approach Results:")
print("-" * 54)
print(f"Input: [1, 2, 3, 1] => Output: {SolutionSorting().containsDuplicate([1, 2, 3, 1])}")
print(f"Input: [1, 2, 3, 4] => Output: {SolutionSorting().containsDuplicate([1, 2, 3, 4])}")
print(f"Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] => Output: {SolutionSorting().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])}")
print()

# Set approach
print("-" * 54)
print("Set Approach Results:")
print("-" * 54)
print(f"Input: [1, 2, 3, 1] => Output: {SolutionSet().containsDuplicate([1, 2, 3, 1])}")
print(f"Input: [1, 2, 3, 4] => Output: {SolutionSet().containsDuplicate([1, 2, 3, 4])}")
print(f"Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] => Output: {SolutionSet().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])}")
