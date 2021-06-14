def exclusive_binary_search(nums:list, target:int) -> int:
    """
    searches a sorted list of intergers and returns the index of the target if the target is in the array.
    If target is not in the list, -1 is returned. 
    """
    # get the bounds of the array
    l, r = 0, len(nums)-1

    # check if we have received a valid array
    if l > r:
        return -1


    while l <= r:
        m = (l + r) // 2
        if target == nums[m]: return m
        elif target > nums[m]: l = m + 1
        elif target < nums[m]: r = m - 1

    return -1 

def inclusive_binary_search(nums:list, target:int) -> int:
    """
    searches a sorted list of intergers and returns the index of the target. 
    If the target is not in the list, returns the index of where it should be
    """
    # get the bounds of the array
    l, r = 0, len(nums)-1

    # check if we have received a valid array
    if l > r:
        return -1
    
    # check to see if the target is out of the bounds of the array
    elif target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)

    while l <= r:
        m = (l + r) // 2
        if target == nums[m]: return m
        elif target < nums[m] and target > nums[m-1]: return m
        elif target > nums[m]: l = m + 1
        elif target < nums[m]: r = m - 1

def main():
    data = [1, 2, 3, 5]
    point = 6
    val = inclusive_binary_search(data, point)
    print(val)

if __name__ == '__main__':
    main()