def merge(nums1, nums2):
    if not nums2:
        return nums1
    if not nums1:
        return nums2
    if nums1[0] <= nums2[0]:
        return [nums1[0]] + merge(nums1[1:], nums2)
    else:
        return [nums2[0]] + merge(nums1, nums2[1:])

def mergesort(array):
    if len(array) > 1:
        array1 = mergesort(array[:len(array)//2])
        array2 = mergesort(array[len(array)//2:])
        return merge(array1, array2)
    else:
        return array
    
input = [9,8,7,6,5,4,3,2,1]

output = mergesort(input)
print(output) 