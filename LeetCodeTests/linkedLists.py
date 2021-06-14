"""
@brief: class for a singley linked list. To be used alongside appropriate singley list functions. 
@param: val - the value that the node can take. 
@param: next - an instance of another node that will apear next in the list. 
"""
class SingleNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next 

"""
@breif: class to implement a singley linked list. List pointed to the first of a collection of nodes. 
@param: head - the first node in the list.
"""
class SingleList:
    def __init__(self, head=None) -> None:
        self.head = head

    """
    @breif: prints out the values contained in the singley linked lists. 
    """
    def printList(self):
        printlist = []
        current = self.head
        while current != None:
            printlist.append(current.val)
            current = current.next
        print(printlist)

"""
@brief: inserts a value at the begining of the list. 
@param: l - a singley linked list. 
@param: val - the value to be inserted. 
@return: None 
"""
def insertNode(l: SingleList, val: int) -> None:
    newNode = SingleNode(val)
    newNode.next = l.head
    l.head = newNode

"""
@brief: appends a value at the end of the list. 
@param: l - a singley linked list. 
@param: val - the value to be appended. 
@return: none
"""
def appendNode(l: SingleList, val:int) -> None:
    newNode = SingleNode(val)
    if l.head is None:
        l.head = newNode
        return

    current = l.head
    while current.next != None:
        current = current.next
    current.next = newNode 

"""
@brief: function to delete a value in the list. 
@param: l - a singley linked list. 
@param: val - the value to be removed. 
@return: none
"""
def removeNode(l: SingleList, removeVal:int) -> None:
    current = l.head
    
    #handle a deletion of the first node
    if current.val is removeVal:
        #if this is the only node in the list
        if current.next is None:
            l.head = None
        #if there are other nodes still in the list
        else:
            l.head = current.next
        return
    
    while current.next.next and current.next.val is not removeVal:
        current = current.next

    if current.next.val is removeVal:
        current.next = current.next.next 

"""
@brief: mergers two lists of compatible val types together in ascending order. 
@param: l1 - first list to be merged.
@param: l2 - second list to be merged. 
@return: head.next - a pointer to the merged list. 
"""
def mergeTwoLists(list1: SingleList, list2: SingleList) -> SingleList: 
    # set a head and current pointer to a new ListNode
    head = current = SingleNode(0)
    returnList = SingleList()
    l1, l2 = list1.head, list2.head

    # if we have values in both l1 and l2 we know we have to sort them out. 
    while l1 and l2:

        if l1.val < l2.val:
            current.next = l1
            current = current.next
            l1 = l1.next
        else: #l1.val >= l2.val
            current.next = l2
            current = current.next
            l2 = l2.next

    # we may have some remaining in either list so make sure to include those 
    current.next = l1 or l2    
    returnList.head = head.next
    return returnList

def main():

    list1 = SingleList()
    appendNode(list1, 1)
    appendNode(list1, 2)
    appendNode(list1, 1)

    list1.printList()

if __name__ == '__main__':
    main()
