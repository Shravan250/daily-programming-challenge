# You are given an array arr containing n-1 distinct integers. The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence. Your task is to find the missing integer.
# Example
# arr = [1, 2, 4, 5]
# Output: 3


def find_missing(arr, n):
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum

def main():
    arr = [1, 2, 4, 5]
    n = 5
    print(find_missing(arr, n))

if __name__ == "__main__":
    main()