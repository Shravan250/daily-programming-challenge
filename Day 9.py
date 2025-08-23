# Problem : Longest Common Prefix
# You are given an array of strings strs[], consisting of lowercase letters. Your task is to find the longest common prefix shared among all the strings. If there is no common prefix, return an empty string "".
# A common prefix is a substring that appears at the beginning of all the strings in the array. The task is to identify the longest such prefix that all strings share.

# Input :
# An array of strings strs[] where each string consists of lowercase English letters.
# Input: strs[] = ["flower", "flow", "flight"]

# Output :
# A string representing the longest common prefix. If no common prefix exists, return an empty string "".
# Output: "fl"
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix
    
    
def main():
    strs = ["flower", "flow", "flight"]
    result = longest_common_prefix(strs)
    print("Output:", result)

if __name__ == "__main__":
    main()