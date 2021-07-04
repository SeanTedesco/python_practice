def length_of_longest_substring_hash_set(s:str) -> int:
    chars = [0]*128

    left = right = 0
    
    res = 0
    while right <len(s):
        # add in the new character from the string to the hash
        r = s[right]
        chars[ord(r)] += 1

        while chars[ord(r)] > 1:
            # remove the duplicate character 
            l = s[left]
            chars[ord(l)] -= 1
            left += 1

        res = max(res, right-left+1)

        right += 1

    return res

def length_of_longest_substring_mapping(s:str) -> int:
    """
    Time Complexity: O(n) - we go through the list only once with index j, moving index i to where any duplicates are. 
    Space Complexity: O(min(n,m) - where n is the length of the string, and m is the length of the character set.
        The size of the map has an upper bound dependent on the minimum of these values. 
    """

    n = len(s)
    ans = 0

    # store index of character
    mp = {}

    # i = left index, j = right index of window
    i = 0
    for j in range(n):

        # if this character is already in the window...
        if s[j] in mp:

            # move the left index to the index of the character that is the immediate next after this duplicate. 
            i = max(mp[s[j]], i)

        # compare the current window length to the maximum one we have seen 
        ans = max(ans, j-i+1)

        # keep track of the index that this character has been seen at 
        mp[s[j]] = j + 1

    # after moving through the entire array, return the 
    return ans

def main():
    s = "abcabcac"
    val = length_of_longest_substring_mapping(s)
    for i in range(5):
        print(i%3)

if __name__ == '__main__':
    main()