from solution import min_remove_parentheses

def is_valid_parentheses(s):
    """
    Helper function to check if parentheses in a string are valid.
    """
    count = 0
    for ch in s:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


def run_test(s):
    result = min_remove_parentheses(s)

    print("Input:  ", s)
    print("Output: ", result)

    if is_valid_parentheses(result):
        print("✅ Test PASSED\n")
    else:
        print("❌ Test FAILED\n")


# Test cases
run_test("lee(t(c)o)de)")
run_test("a)b(c)d")
run_test("))((")
run_test("(a(b(c)d)")
