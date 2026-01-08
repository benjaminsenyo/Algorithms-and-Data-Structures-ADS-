def min_remove_parentheses(s):
    """
    Remove the minimum number of parentheses to make the string valid.

    A string is valid if every opening '(' has a matching closing ')'
    and parentheses are properly nested.

    Parameters
    ----------
    s : str
        Input string containing lowercase letters and parentheses.

    Returns
    -------
    str
        A valid string with minimum removals.
    """
    stack = []
    remove = set()

    # First pass: mark invalid parentheses
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

    # Build result string
    result = []
    for i, ch in enumerate(s):
        if i not in remove:
            result.append(ch)

    return ''.join(result)
