from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Return all unique triplets [a, b, c] in nums such that a + b + c == 0.
    """
    nums.sort()
    n = len(nums)
    res: List[List[int]] = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicate first element
        a = nums[i]
        left, right = i + 1, n - 1

        while left < right:
            s = a + nums[left] + nums[right]
            if s == 0:
                res.append([a, nums[left], nums[right]])
                # skip duplicates for left and right
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1

    return res

# Example usage:
if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))