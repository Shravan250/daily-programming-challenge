# You are given an array arr consisting only of Os, ls, and 2s.
# The task is to sort the array in increasing order in linear time (i.e., 0(n))
# without using any extra space.
# This means you need to
# rearrange the array in-place.
#
# Example 1
# arr = [0, 1, 2, 1, 0, 2, 1, 0]
# Output: [0, 0, 0, 1, 1, 1, 2, 2]


def sort_arr(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    

def main():
    arr = [0, 1, 2, 1, 0, 2, 1, 0]
    sort_arr(arr)
    print(arr)

if __name__ == "__main__":
    main()