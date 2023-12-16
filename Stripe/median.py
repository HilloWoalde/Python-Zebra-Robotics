def findMedianSortedArrays(nums1_str, nums2_str):
    # Convert the string representations to lists of integers
    nums1 = [int(num) for num in nums1_str.strip('[], \r, \n').split(', ')]
    nums2 = [int(num) for num in nums2_str.strip('[], \r, \n').split(', ')]

    # Merge the two sorted arrays
    merged_array = mergeArrays(nums1, nums2)

    # Find the length of the merged array
    length = len(merged_array)

    # Check if the length is even or odd
    if length % 2 == 0:
        # If even, calculate the average of the middle two elements
        mid_right = length // 2
        mid_left = mid_right - 1
        median = (merged_array[mid_left] + merged_array[mid_right]) / 2
    else:
        # If odd, the median is the middle element
        mid = length // 2
        median = merged_array[mid]

    return median

def mergeArrays(nums1, nums2):
    # Merge the two sorted arrays without using .sort()
    merged = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Add remaining elements from both arrays, if any
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    return merged

# usage
nums1_str = input()
nums2_str = input()
result = findMedianSortedArrays(nums1_str, nums2_str)
print(result)