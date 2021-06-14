haystack = "Hello World!"
needle = "or"

def is_in_string(needle: str="", haystack: str="") -> int:
    
    #make sure we are receiving sufficient input parameters
    if needle == "" or haystack == "" or len(needle) > len(haystack):
        return 0

    # create the prefix/suffix table
    lps = create_partial_match_table(needle)

    i, j = 0, 0
    while i < len(haystack):

        # the current characters match, so move on to the next
        if haystack[i] == needle[j]:
            i += 1
            j += 1

        # now if they do not match...
        else: 
            if j > 0:
                # try to start with the previous found longest prefix
                j = lps[j-1]
            else:
                # move on to the next character in the haystack
                i += 1
        
        # check to see if we have gone the length on the needle
        if j == len(needle):

            # if we have reached the end of the needle, return the begining 
            return i - len(needle)

    # no match found if we leave the while loop      
    return -1

def create_partial_match_table(pattern: str=""):

    # make sure we receive a pattern to build the table
    if pattern == "":
        return -1

    # create an empty table, first value will always be 0
    lps = [0] * len(pattern)

    i, j = 1, 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            # we have a reoccuring chacter so the longest prefix/suffix grows
            lps[i] = j + 1
            j += 1
            i += 1
        else:
            if j > 0:
                # move back to where we have a proper prefix
                j = lps[j-1]
            else: 
                # j == 0 so no pattern yet, move onto next character
                lps[i] = 0
                i += 1
    return lps

def print_title(title: str=""):
    print("------------------------")
    print(f"     {title}")
    print("------------------------")
    print()

def main():
    print_title("KMP Algorithm")
    print(f"Looking for '{needle}' in '{haystack}'\n\r")
    index = is_in_string(needle, haystack)

    if index > 0:
        print(f"Found '{needle}' at location {index} in '{haystack}'!\r\n")
    elif index < 0:
        print(f"No occurance of '{needle}' in '{haystack}'\r\n")
    else:
        print("Error\r\n")

if __name__ == '__main__':
    main()