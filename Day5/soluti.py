def merge_intervals(intervals):
    """
    Merge all overlapping intervals.

    Parameters
    ----------
    intervals : list of list of int
        A list where each element is [start, end].

    Returns
    -------
    list of list of int
        Merged non-overlapping intervals.
    """
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
