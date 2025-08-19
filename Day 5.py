# Problem : Find the Leaders in an Array
# You are given an integer array arr of size n. An element is considered a leader if it is greater than all the elements to its right. Your task is to find all such leader elements in the array.

# Input :
# An integer array arr of size n.
# Example : 
# arr = [16, 17, 4, 3, 5, 2]

# Output :
# Return an array containing all the leader elements in the order in which they appear in the original array.
# Example:
# Leaders: [17, 5, 2]

def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[n - 1]
    leaders.append(max_from_right)

    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)

    return leaders[::-1]

def main():
    arr = [16, 17, 4, 3, 5, 2]
    leaders = find_leaders(arr)
    print("Leaders:", leaders)

if __name__ == "__main__":
    main()