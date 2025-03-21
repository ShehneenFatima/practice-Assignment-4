#Given an array, Rotate (shift left) an array of n elements to the right by k steps.
#For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated
#to [5,6,7,1,2,3,4].
#After rotating the array add in into another array and display array index with
#minumum value
def rotate_array(arr, k):
    k = k % len(arr)
    rotated_arr = arr[-k:] + arr[:-k]
    return rotated_arr

def find_min_index(arr):
    min_value = min(arr)
    return arr.index(min_value)

n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter space-separated array elements: ").split()))
k = int(input("Enter number of rotation steps: "))

rotated_arr = rotate_array(arr, k)
min_index = find_min_index(rotated_arr)

print("Rotated Array:", rotated_arr)
print("Index of Minimum Value:", min_index)

