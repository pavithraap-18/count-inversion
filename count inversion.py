def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0  # Count of inversions

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # Elements left in left subarray are inversions
            j += 1
        k += 1

    while i <= mid:  # Copy remaining elements of left subarray
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:  # Copy remaining elements of right subarray
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):  # Copy sorted elements back to original array
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def count_inversions(arr):
    temp_arr = arr.copy()
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

# Example usage
arr = [2, 4, 1, 3, 5]
print("Number of inversions:", count_inversions(arr))
