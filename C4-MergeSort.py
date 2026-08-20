def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare elements from left and right halves and merge in order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

"""
How it works

- Divide: Split the array into two halves around the middle index.
- Conquer: Recursively sort each half until reaching the base case (an array of length 0 or 1, which is already sorted).
- Combine: Merge the two sorted halves by repeatedly comparing the smallest remaining elements from each half and appending the smaller one to the output.
- Using the comparison left[i] <= right[j] (take from left on ties) preserves the original relative order of equal elements.

Performance metrics

- Time complexity: O(n log n) for worst, average, and best cases. The recursion depth is O(log n) (repeated halving)
- each level performs a linear-time merge of all elements, giving O(n) work per level.
- Space complexity: O(n) auxiliary space in the usual merge implementation because merging requires a temporary array to hold the combined results.
- Stability: Stable — when ties are broken by taking from the left subarray first (<=), equal elements keep their original relative order.
"""