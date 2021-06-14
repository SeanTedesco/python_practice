class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return str.format("Make: {}, Model: {}, Year: {}", self.make, self.model, self.year)

def merge_sort(nums: list, left:int, right:int):
    """
    sorts list of nums into ascending order using a top-down implementation
    """

    # this is our stop condition for the recursive call
    if left >= right:
        return
    
    # split entire list into many left and right lists
    middle = (left+right)//2
    merge_sort(nums, left, middle)
    merge_sort(nums, middle+1, right)

    # finally merge all the lists together 
    merge(nums, left, right, middle)

def merge(n:list, l:int, r:int, m:int):
    """
    Helper function for merge_sort_recursive. 
    Performs the merge while returning up the call chain.
    """
    
    # make copies of our lists
    l_copy = n[l:m+1]
    r_copy = n[m+1:r+1]

    # set up list indexes 
    l_idx = 0
    r_idx = 0
    s_idx = l

    # sort elements in both lists until we run out of atleast one list
    while l_idx < len(l_copy) and r_idx < len(r_copy):
        
        # replace elements in nums by comparing left to right
        if l_copy[l_idx] <= r_copy[r_idx]:
            n[s_idx] = l_copy[l_idx]
            l_idx += 1
        else:
            n[s_idx] = r_copy[r_idx]
            r_idx += 1

        s_idx += 1

    # append any of the remaining values that may still be in either list. 
    while l_idx < len(l_copy):
        n[s_idx] = l_copy[l_idx]
        l_idx += 1
        s_idx += 1
    while r_idx < len(r_copy):
        n[s_idx] = r_copy[r_idx]
        r_idx += 1
        s_idx += 1

def merge_sort_objects(array: list, left:int, right:int, comparison):
    # this is our stop condition for the recursive call
    if left >= right:
        return
    
    # split entire list into many left and right lists
    middle = (left+right)//2
    merge_sort_objects(array, left, middle)
    merge_sort_objects(array, middle+1, right)

    # finally merge all the lists together 
    merge_objects(array, left, right, middle, comparison)

def merge_objects(a:list, l:int, r:int, m:int, comparison):
        # make copies of our lists
    l_copy = a[l:m+1]
    r_copy = a[m+1:r+1]

    # set up list indexes 
    l_idx = 0
    r_idx = 0
    s_idx = l

    # sort elements in both lists until we run out of atleast one list
    while l_idx < len(l_copy) and r_idx < len(r_copy):
        
        # replace elements in nums by comparing left to right
        if comparison(l_copy[l_idx], r_copy[r_idx]):
            a[s_idx] = l_copy[l_idx]
            l_idx += 1
        else:
            a[s_idx] = r_copy[r_idx]
            r_idx += 1

        s_idx += 1

    # append any of the remaining values that may still be in either list. 
    while l_idx < len(l_copy):
        a[s_idx] = l_copy[l_idx]
        l_idx += 1
        s_idx += 1
    while r_idx < len(r_copy):
        a[s_idx] = r_copy[r_idx]
        r_idx += 1
        s_idx += 1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str.format("({},{})", self.x, self.y)

def insertion_sort(nums: list):

    # handle empty and 1 element list
    if nums == [] or len(nums) == 1:
        return nums

    # we must go through the entire list once
    for i in range(1, len(nums)):
        current = nums[i]
        index = i

        # move items to the right of the list until we find a value that is less than our unsorted one. 
        while index > 0 and nums[index-1] > current:
            nums[index] = nums[index-1]
            index -= 1
        
        # we have now found the right spot, whether at the begining or in the middle of the list. 
        nums[index] = current

def insertion_sort_objects(objs: list, comparison):
    if objs == [] or len(objs) == 1:
        return objs
    
    for i in range(1, len(objs)):
        
        current = objs[i]
        index = i
        while index > 0 and comparison(objs[index-1], current):
            objs[index] = objs[index-1]
            index -= 1
        
        objs[index] = current

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

def quick_sort(nums:list, start:int, end:int):
    if start >= end:
        return
    
    # p will be already "sorted" so we go call again on p-1 and p+1 
    p = partition(nums, start, end)
    quick_sort(nums, start, p-1)
    quick_sort(nums, p+1, end)

def partition(nums: list, start:int, end:int):
    pivot = nums[start]
    low = start + 1
    high = end

    while True: 
        # move down nums, starting at high until a value less than the pivot is found
        while low <= high and nums[high] >= pivot:
            high -= 1
        # move up nums, starting at low until a value greater than the pivot is found
        while low <= high and nums[low] <= pivot:
            low += 1

        # check what caused the break from the inner while loops
        if low <= high:
            # low and high didn't intersect so we found a value, make the swap
            nums[high], nums[low] = nums[low], nums[high]
        else:
            # low and high did interset, no value found, this list is sorted 
            break

    # swap the pivot element, the one at the start with the last value we ended with 
    nums[start], nums[high] = nums[high], nums[start]

    # return the pivot index to be used in quick sort
    return high

def quick_sort_objects(objs:list, start:int, end:int, comparison):
    # this has the same implementation as quick sort with integer list. 
    if start >= end:
        return
    
    # p will be already "sorted" so we go call again on p-1 and p+1 
    p = partition_objects(objs, start, end, comparison)
    quick_sort_objects(objs, start, p-1, comparison)
    quick_sort_objects(objs, p+1, end, comparison)

def partition_objects(objs: list, start:int, end:int, comparison):
    pivot = objs[start]
    low = start + 1
    high = end

    while True: 
        # move down nums, starting at high until a value less than the pivot is found
        while low <= high and comparison(objs[high], pivot):
            high -= 1
        # move up nums, starting at low until a value greater than the pivot is found
        while low <= high and not comparison(objs[low], pivot):
            low += 1

        # check what caused the break from the inner while loops
        if low <= high:
            # low and high didn't intersect so we found a value, make the swap
            objs[high], objs[low] = objs[low], objs[high]
        else:
            # low and high did interset, no value found, this list is sorted 
            break

    # swap the pivot element, the one at the start with the last value we ended with 
    objs[start], objs[high] = objs[high], objs[start]

    # return the pivot index to be used in quick sort
    return high

def heap_sort(nums: list):
    pass

def main():
####################################### MERGE SORT ###############################################################
    """
    Time Complexity: O(n*log(n)) - log(n) time for splitting array and n (linear) time for merging array
    Space Complexity: O(n) - we keep a copy of each of the elements in the original list
    """
    """
    # MERGE SORT RECURSIVE
    data = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
    merge_sort_recursive(data, 0, len(data))
    print(data)
    """
    """
    # MERGE SORT OBJECTS
    car1 = Car("Alfa Romeo", "33 SportWagon", 1988)
    car2 = Car("Chevrolet", "Cruze Hatchback", 2011)
    car3 = Car("Corvette", "C6 Couple", 2004)
    car4 = Car("Cadillac", "Seville Sedan", 1995)

    array = [car1, car2, car3, car4]

    merge_sort(array, 0, len(array) -1, lambda carA, carB: carA.year < carB.year)

    print("Cars sorted by year:")
    for car in array:
        print(car)
    """
####################################### INSERTION SORT ###########################################################
    """
    Time Complexity: O(n^2) for worst and average cases, O(n) for best case. 
    Space Complexity: O(1) no extra space is required. 
    """
    """
    # INSERTION SORT
    data = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
    insertion_sort(data)
    print(data)
    """
    """
    # INSERTION SORT OBJECTS 
    A = Point(1,2)
    B = Point(4,4)
    C = Point(3,1)
    D = Point(10,0)
    array = [A,B,C,D]
    # We sort by the x coordinate, ascending
    insertion_sort_objects(array, lambda a, b: a.x > b.x)
    for point in array:
        print(point)
    """
####################################### QUICK SORT ###############################################################
    """
    Time Complexity: O(n*log(n)) - we make log(n) calls to split the array, then O(n) to sort it again as no call sorts the same part of the array 
    Space Complexity: O(log(n)) - we make log(n) calls to parition as we are constantly splitting the array in half. 
    """
    """
    # QUICK SORT
    array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
    quick_sort(array, 0, len(array) - 1)
    print(array)
    """
    """
    # QUICK SORT OBJECTS
    A = Person("Sean", 24)
    B = Person("Carter", 16)
    C = Person("Maddy", 26)
    D = Person("Caity", 26)
    array = [A, B, C, D]
    quick_sort_objects(array, 0, len(array)-1, lambda x, y: x.age < y.age)
    for person in array:
        print(person)
    """


if __name__ == '__main__':
    main()