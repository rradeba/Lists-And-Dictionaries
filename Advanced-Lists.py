# Task 1 
# Time complexity: O(n), where n is the combined length of dict1 and dict2 
# Space Complexity: O(n), where n is the total key-value pairs in the combined dictionaries 


def merge_dictionaries(dict1, dict2):
 
    merged_dict = dict1.copy()
    
    
    merged_dict.update(dict2)
    
    return merged_dict



# Task 2
# Time complexity: O(n), where n is the length of dict1 
# Space Complexity: O(n), where n is the length of the keys that are shared 


def intersect_dictionaries(dict1, dict2):
    intersection = {key: dict1[key] for key in dict1 if key in dict2}
    return intersection


# Task 3
# Time complexity: O(n), where n is the number of words in the original list
# Space Complexity: O(n), where n is the number of unique words

def word_freq(word_list):
    
    freq_dict = {}

    for word in word_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
            
    return freq_dict

