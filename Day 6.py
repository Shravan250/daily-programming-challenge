# Problem : Find All Subarrays with Zero Sum
# You are given an integer array arr of size n. Your task is to find all the subarrays whose elements sum up to zero. A subarray is defined as a contiguous part of the array, and you must return the starting and ending indices of each subarray.

# Input :
# An integer array arr of size n where n represents the number of elements in the array.
# Example : 
# Input: [1, 2, -3, 3, -1, 2]

# Output :
# •⁠  ⁠Return a list of tuples, where each tuple contains two integers. The starting index (0-based) of the subarray. The ending index (0-based) of the subarray.
# •⁠  ⁠The output should list all subarrays that sum to zero. If no such subarrays are found, return an empty list.
# Example
# Output: [(0, 2), (1, 3)]


def find_zero_sum_subarrays(arr):
    n = len(arr)
    zero_sum_subarrays = []
    prefix_sum = 0
    sum_indices = {}

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum == 0:
            zero_sum_subarrays.append((0, i))

        if prefix_sum in sum_indices:
            for start_index in sum_indices[prefix_sum]:
                zero_sum_subarrays.append((start_index + 1, i))
        
        if prefix_sum not in sum_indices:
            sum_indices[prefix_sum] = []
        sum_indices[prefix_sum].append(i)

    return zero_sum_subarrays

def main():
    arr = [1, 2, -3, 3, -1, 2]
    result = find_zero_sum_subarrays(arr)
    print("Output:", result)

if __name__ == "__main__":
    main()