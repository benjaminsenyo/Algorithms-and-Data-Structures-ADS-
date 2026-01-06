"""
START
Input array nums and integer target

Sort nums

Create empty list result

FOR i from 0 to length(nums) - 4:
    FOR j from i + 1 to length(nums) - 3:
        Set left = j + 1
        Set right = last index

        WHILE left < right:
            sum = nums[i] + nums[j] + nums[left] + nums[right]

            IF sum equals target:
                Add quadruplet to result
                Move left forward
                Move right backward

            ELSE IF sum < target:
                Move left forward

            ELSE:
                Move right backward

RETURN result
END

"""

def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    quad = [nums[i], nums[j], nums[left], nums[right]]
                    if quad not in result:
                        result.append(quad)
                    left += 1
                    right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result
