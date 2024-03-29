import random


def gen_array(size=100):
    A = []
    for _ in range(size):
        A.append(random.randint(0, size))
    return A


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float("-inf")
    summarize = 0

    for i in range(mid, low - 1, -1):
        summarize += A[i]

        if summarize > left_sum:
            left_sum = summarize
            max_left = i

    right_sum = float("-inf")
    summarize = 0

    for j in range(mid + 1, high + 1, 1):
        summarize += A[j]

        if summarize > right_sum:
            right_sum = summarize
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_max_subarray(A, low, high):
    if high == low:  # only one element
        return low, high, A[low]
    else:
        mid = (low + high) // 2

        left_low, left_high, left_sum = find_max_subarray(A, low, mid)
        right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum
