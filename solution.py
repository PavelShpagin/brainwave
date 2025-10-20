#!/usr/bin/env python3

def get_letter_set(word):
    """Get sorted unique letters from a word"""
    return ''.join(sorted(set(word.lower())))

def word_to_number(words):
    """
    Map words to numbers based on unique letter sets.
    Each unique letter set gets assigned the next available index
    in order of first appearance.
    """
    letter_set_to_index = {}
    results = []
    next_index = 0
    
    for word in words:
        letter_set = get_letter_set(word)
        
        if letter_set not in letter_set_to_index:
            letter_set_to_index[letter_set] = next_index
            next_index += 1
        
        results.append(letter_set_to_index[letter_set])
    
    return results

# Read input
n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())

# Get results
results = word_to_number(words)

# Print results
for r in results:
    print(r)
