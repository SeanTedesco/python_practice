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

###############################################################

l1 = 5
l2 = 5

carry = (l1+l2) // 10 
keep = (l1+l2) % 10

print(keep, carry)