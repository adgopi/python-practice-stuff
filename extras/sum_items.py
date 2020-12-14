def sum_items(list1, list2):
    '''(list of numbers, list of numbers) -> list of number
    
    Return a new list which sums items at corresponding indices of list1 and list 2

    Precondition: len(list1) == len(list2)

    >>> sum_items([1,2,3] , [4,5,6])
    [5,7,9]
        
    '''
    sum_list = []

    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return sum_list
