from solution import merge_intervals

def run_test(intervals, expected):
    result = merge_intervals([i[:] for i in intervals])

    print("Input:    ", intervals)
    print("Expected: ", expected)
    print("Output:   ", result)

    if result == expected:
        print("✅ Test PASSED\n")
    else:
        print("❌ Test FAILED\n")

# Run tests
run_test([[1,3],[2,6],[8,10],[15,18]],
         [[1,6],[8,10],[15,18]])

run_test([[1,4],[4,5]],
         [[1,5]])
