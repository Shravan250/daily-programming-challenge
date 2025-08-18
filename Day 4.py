# You are given two sorted arrays arri of size m and arr2 of size n.Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). The
# elements in arri should be merged first, followed by the elements of arr2, resulting in both arrays being sorted after the merge.

# Example 
# Input:
# arr1 = [1, 3, 5, 7]
# arr2 = [2, 4, 6, 8]
# Output:
# arr1 = [1, 2, 3, 4]
# arr2 = [5, 6, 7, 8]


def merge_in_place(arr1, arr2):
    m, n = len(arr1), len(arr2)

    for i in range(m):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]

            first = arr2[0]
            k = 1
            while k < n and arr2[k] < first:
                arr2[k - 1] = arr2[k]
                k += 1
            arr2[k - 1] = first


def main():
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    merge_in_place(arr1, arr2)
    print("arr1:", arr1)
    print("arr2:", arr2)

if __name__ == "__main__":
    main()