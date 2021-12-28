from typing import List
"""
strs = ["ab","a"]


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
"""
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
"""
################################################################
"""from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        current = nums[0]
        max_sum = current
        
        for i in range(1, len(nums)):
            
            current = max(nums[i], current + nums[i])
            max_sum = max(max_sum, current)
                
        return max_sum
"""
################################################################

"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = digits

        i, carry = len(digits)-1, 1
        while carry:

            if i == -1:
                digits.insert(0, 1)
                break

            value = digits[i] + carry
            summ, carry = value % 10, value // 10
            digits[i] = summ
            i -= 1
            print(f"sum: {summ}, carry: {carry}")
                
        return digits
"""
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            j = m + i
            
            nums1[j] = nums2[i]  
            
            while nums1[j] < nums1[j-1] and j-1 >= 0:
                nums1[j], nums1[j-1] = nums1[j-1], nums1[j]
                j -= 1
            
            if j-1 == 0 and nums1[j] < nums1[j-1]:
                nums1[j], nums1[j-1] = nums1[j-1], nums1[j]
"""
"""class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        while m > 0 and n > 0:

            # if nums1 has the bigger element
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                # nums2 has the bigger element
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        
        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1




nums1 = [6, 7, 0]
nums2 = [2]

n = len(nums2)
m = len(nums1) - len(nums2)
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)
"""
################################################################
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            value = nums.pop(0)
            if value in nums:
                return True
            
        return False
"""
################################################################
"""
class Solution:
    def tribonacci(self, n: int) -> int:
 
        #Tn = Tn-3 + Tn-2 + Tn-1 for n >= 
        
        memo = {}
        
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        
        if (n-3) not in memo: memo[n-3] = self.tribonacci(n-3)
        if (n-2) not in memo: memo[n-2] = self.tribonacci(n-2)
        if (n-1) not in memo: memo[n-1] = self.tribonacci(n-1)
        
        return memo[n-3] + memo[n-2] + memo[n-1] 

solution = Solution()
answer = solution.tribonacci(25)
print(answer )
"""

################################################################
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        current = []
        
        current.append(cost[0])
        current.append(cost[1])
        
        for i in range(2, len(cost)):
            current.append( (cost[i] + min(current[i-2], current[i-1])) )
            print(cost[i], min(cost[i-2], cost[i-1]))
            print(current)
            
            
        return min(current[-1], current[-2])
"""
################################################################
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        
        nums.sort()

        return nums
"""
################################################################
"""
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        print(nums, k)


        print(nums[2:], nums[:2])

        nums[:] = nums[n-k:] + nums[:n-k]
"""
################################################################
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        Do not return anything, modify nums in-place instead.
        
        1st idea: bubble up the zeros
        - 2 pointers, one pointing an next available zero,
        another moving.
        - move until integer is found, swap integer and zero
        - must go through entire list. 
        Time: 
        Space: O(1)
        '''
        
        if len(nums) == 1: return
        
        i, swaps = 0, 0
        while i < (len(nums) - swaps):
            if nums[i] == 0:
                nums.append(nums.pop(i))
                swaps += 1
            else:
                i += 1
            print(i, nums)
"""
################################################################
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        points = 0
        deleted = []
        for i in range(len(nums)):
            current = nums[i]
            deleted.append(nums[i]+1)
            deleted.append(nums[i]-1)
    
            j = 0
            while j < len(nums):
                print(f'seed:{nums[i]}, add?: {nums[j]}')
                print(f'deleted: {deleted}')
                if nums[j] not in deleted and j != i:
                    current += nums[j]
                    deleted.append(nums[j]+1)
                    deleted.append(nums[j]-1)
                    print(f'current: {current}')
                j += 1
            
            
            deleted = []

            points = max(current, points)
            
        return points
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle = list()

        triangle.append([1])
        if numRows == 1: return triangle
        
        for row in range(1, numRows-1):

            new_row = list()

            for col in range(-1, row):

                if col == -1 or col == row-1: 
                    new_row.append(1)
                    continue

            triangle.append(new_row)








solution = Solution()
answer = solution.generate(5)
print(answer)