# Problem : Group Anagrams
# You are given an array of strings strs[]. Your task is to group all the strings that are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# The goal is to return the grouped anagrams as a list of lists, where each sublist contains words that are anagrams of each other.

# Input :
# An array of strings strs[] consisting of lowercase English letters.
# Input: strs[] = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Output :
# A list of lists, where each sublist contains strings that are anagrams of each other. The order of the output groups does not matter.
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def group_anagrams(strs):
    anagrams = {}
    
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    
    return list(anagrams.values())      

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    print("Output:", result)    

if __name__ == "__main__":
    main()