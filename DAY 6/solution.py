def min_remove_parentheses(s):
    """
    QUESTION:
    Given a string s containing lowercase English letters and the characters
    '(' and ')', remove the minimum number of parentheses so that the resulting
    string is valid.

    A string is considered valid if:
    - Every opening parenthesis '(' has a corresponding closing parenthesis ')'
    - Parentheses are properly nested

    PARAMETERS:
    ----------
    s : str
        Input string containing lowercase letters and parentheses.

    RETURNS:
    -------
    str
        A valid string obtained by removing the minimum number of parentheses.

    EXAMPLE:
    --------
    Input:  "a)b(c)d"
    Output: "ab(c)d"
    """

    stack = []
    remove = set()

    # First pass: identify invalid parentheses
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                remove.add(i)

    # Any unmatched '(' are invalid
    remove.update(stack)

    # Build the valid result string
    result = []
    for i, ch in enumerate(s):
        if i not in remove:
            result.append(ch)

    return ''.join(result)
