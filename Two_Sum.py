#!/usr/bin/env python3
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Return indices of the two numbers such that they add up to target.
    Raises ValueError if no solution exists.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("No two sum solution")

if __name__ == "__main__":
    # Example usage
    arr = [2, 7, 11, 15]        
    tgt = 9
    print(two_sum(arr, tgt))  # prints [0, 1]