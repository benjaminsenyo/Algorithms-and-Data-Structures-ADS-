from solu import sort_colors

def run_test(nums, expected):
    result = sort_colors(nums.copy())  # avoid modifying original input
    print("Input:    ", nums)
    print("Expected: ", expected)
    print("Output:   ", result)

    if result == expected:
        print("✅ Test PASSED\n")
    else:
        print("❌ Test FAILED\n")

# Test cases
run_test([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])
run_test([2, 0, 1], [0, 1, 2])
run_test([0], [0])
run_test([1, 2, 0], [0, 1, 2])
