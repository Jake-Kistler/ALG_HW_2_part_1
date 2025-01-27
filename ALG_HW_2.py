import math

def find_n_by_binary_search(c=8.64e13):
    """
    Finds the largest integer n such that n*log2(n) <= c,
    using a binary search approach.
    """
    # We'll guess n is somewhere between 1 and a high bound.
    # For c = 8.64e13, we know n won't be astronomically huge,
    # but let's pick a safe upper bound. For instance, 
    # we can pick 10^15 or so, or do a dynamic approach.

    low = 1
    high = 10**15  # a guess that's surely above the needed n

    while low < high:
        mid = (low + high) // 2
        lhs = mid * math.log2(mid) if mid > 1 else 0

        if lhs == c:
            return mid  # exact match (rare with logs)
        elif lhs < c:
            # mid is too small or might be exact, so try bigger
            low = mid + 1
        else:
            # mid is too big
            high = mid

    # After the loop, low == high, but we might have overshot by 1
    # Check if n*log2(n) > c, decrement if needed:
    if low * math.log2(low) > c:
        low -= 1

    return low

if __name__ == "__main__":
    solution_bs = find_n_by_binary_search(8.64e13)
    print("Largest n such that n*log2(n) <= 8.64e13 is:", solution_bs)
