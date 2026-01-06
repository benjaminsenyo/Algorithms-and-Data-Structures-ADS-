from solu import four_sum

def run_test(nums, target, expected):
    result = four_sum(nums, target)

    print("Input array: ", nums)
    print("Target:      ", target)
    print("Expected:    ", expected)
    print("Output:      ", result)

    if sorted(result) == sorted(expected):
        print("✅ Test PASSED\n")
    else:
        print("❌ Test FAILED\n")

# Test cases
run_test([1, 0, -1, 0, -2, 2], 0,
         [[-2, -1, 1, 2],
          [-2,  0, 0, 2],
          [-1,  0, 0, 1]])

run_test([2, 2, 2, 2, 2], 8,
         [[2, 2, 2, 2]])

run_test([0, 0, 0, 0], 0,
         [[0, 0, 0, 0]])
