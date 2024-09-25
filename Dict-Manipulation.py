# Task 1 
# The loop iterates n-1  number of times, so the time comlexity is O(n) 
# The resulting list will have n-1 elements, so size will be O(n)

def square_values(n):
    squares = [x**2 for x in range(n)]
    return(squares)


#Task 2 
# Time Complexity: O(n) iterates through sublist n times where n is jthe length 
# Space complexity: O(n) lengt will be n were n is length of subset

def reverse_sublist(list, i, j):
    list[i:j + 1] = list[i:j + 1][::-1]


#Task 3 
# Time Complexity: O(n) where n is the combined length of List 1 and List 2 
# Space Complexity: O(n) where n is the length of the combined lists 

def merge_lists (list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

