from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets [a, b, c] in the list such that a + b + c == 0.
    Returns a list of these triplets.
    """
    nums.sort()
    n = len(nums)
    result: List[List[int]] = []  # renamed for clarity

    for i in range(n - 2):
        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        a = nums[i]
        left, right = i + 1, n - 1

        while left < right:
            total = a + nums[left] + nums[right]
            if total == 0:
                result.append([a, nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for left and right pointers
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# Example usage:
if __name__ == "__main__":
    print("3-sum results:", three_sum([-1, 0, 1, 2, -1, -4]))

# Minor update for PR testing — changed variable names and docstring
