
"""
Pseudocode

START
Input array nums

Count how many 0s, 1s, and 2s are in the array

Overwrite the array:
    First fill with all 0s
    Then fill with all 1s
    Then fill with all 2s

RETURN the sorted array
END

"""
def sort_colors(nums):
    count0 = nums.count(0)
    count1 = nums.count(1)
    count2 = nums.count(2)

    index = 0

    for _ in range(count0):
        nums[index] = 0
        index += 1

    for _ in range(count1):
        nums[index] = 1
        index += 1

    for _ in range(count2):
        nums[index] = 2
        index += 1

    return nums



