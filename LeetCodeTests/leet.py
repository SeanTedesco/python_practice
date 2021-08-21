"""strs = ["ab","a"]


def longestCommonPrefix(strs):
    prefix = ""

    strs.sort()

    if len(strs) == 1:
        return strs[0]

    for word in strs:
        if not word.isalpha():
            return prefix

    current_word = strs[1]

    for i in range(len(current_word)):
        
        prefix = current_word[0:i+1]

        for word in strs:
            if word[0:i+1] != prefix:
                return current_word[0:i]


temp = longestCommonPrefix(strs)
print(temp)
"""
############################################################

"""s = "{[}]"   

# handle empty and odd length string
if len(s) == 0 or len(s) % 2 == 1:
    print(False) 

stack = []
stack_index = -1; 

parentheses = {")": "(", "]": "[", "}": "{"}

for c in s: 
    
    if not stack and c in parentheses.values():
        stack.append(c)
        stack_index += 1
        continue
    elif not stack and c in parentheses.keys():
        print(False)
    
    if c in parentheses.values():
        stack.append(c)
        stack_index += 1
    else:
        if stack[stack_index] == parentheses[c]:
            stack.pop()
            stack_index -= 1
        else:
            print(False)

    print(stack_index)

if not stack:
    print(True)
else: 
    print(False)"""

############################################################
"""
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = []
l2 = []

l1.append(ListNode(1))
l1.append(ListNode(2))
l1[0].next = l1[1]
l1.append(ListNode(6))
l1[1].next = l1[2]

l2.append(ListNode(1))
l2.append(ListNode(4))
l2[0].next = l2[1]
l2.append(ListNode(4))
l2[1].next = l2[2]


index_1 = 0
index_2 = 0        
while l1[index_1].next != None and l2[index_2].next != None:
    
    if l1[index_1].next:
        if l1[index_1].next.val > l2[index_2].val:
            l1.insert(index_1 + 1, l2[index_2])
            l1[index_1 + 1].next = l1[index_1].next
            l1[index_1].next = l1[index_1 + 1]
            index_1 += 1
            index_2 += 1
        
        else: #l1[index_1].next <= l2[index_2].val
            index_1 += 1
    else:
        for i in range(index_2, len(l2)):
            l1.append(l2[i])
            index_2 += 1

for i in l1:
    print(i.val)
"""

###############################################################

"""haystack = "mississippi"
needle = "issipi"

if needle == "":
    print(0)

for i in range(len(haystack)):
    count = 0
    if haystack[i] == needle[0] and len(haystack) - i >= len(needle):
        for j in range(len(needle)):
            if count == len(needle):
                break 

            if haystack[i+j] == needle[j]:
                count += 1
                print(f'Count: {count}')
            else:
                break
    if count == len(needle):
        print(f'found needle: {i}')
print(-1)"""

################################################################
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        palindrome = ''
        
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(palindrome) > j-i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    palindrome = s[i:j]
                    break
        return palindrome

solution = Solution()
answer = solution.longestPalindrome(s = "abcdef")
print(answer)
"""
################################################################
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        palindrome = ''
        
        for i in range(len(s)):
            even = self.found_palindrome_at(s, i, i+1)
            odd = self.found_palindrome_at(s, i, i)

            palindrome = max(palindrome, odd, even, key=len)

        return palindrome

    def found_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
solution = Solution()
answer = solution.longestPalindrome(s = "cababcdef")
print(answer)


# NOTE: Centre can be even or odd.  'abba' or 'cec' 
# Move centre across length of the string finding new protential odd and even seeds. 
# expand from seed matching characters on either side of it to put more elements into the palindrome. 
# compare these even and odds to the existing palindrome and assign the one with the max to length palindrome. 
# O(n^2) runtime - at worst loop through each element in first inner loop and at worst run through second helper loop 0.5n times. 
# O(n) space time - creating new instance of palindrome string. 
"""
################################################################
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1: return s 
     
        current_row = 0
        going_down = False 
        
        rows = []
        for i in range(numRows):
            rows.append([])
        
        for c in s:
            rows[current_row] += c
            
            if current_row == 0 or current_row == numRows-1:
                going_down = not going_down 
                
            current_row = current_row + 1 if going_down else current_row - 1 
            
        zigzag = ''    
        for row in rows:
            for letter in row:
                zigzag += letter
        
        return zigzag 
"""
################################################################
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        left, right = 0, len(height)-1 
        
        while left < right:
            
            length = right-left
            width = min(height[right], height[left])
            max_area = max(max_area, length*width)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area 

solution = Solution()
answer = solution.maxArea(height = [1,8,6,2,5,4,8,3,7])
print(answer)