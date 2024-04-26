def longest_substring(s: str) -> int:
    
    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 
    pass

def longest_substring(s: str) -> int:
   
    max_length = 0
    start = 0
    char_index_map = {}

    
    for end, char in enumerate(s):
       
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        
        
        char_index_map[char] = end
        
        
        max_length = max(max_length, end - start + 1)
    
    return max_length

