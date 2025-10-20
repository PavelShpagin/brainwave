#!/usr/bin/env python3

def get_letter_set(word):
    return ''.join(sorted(set(word.lower())))

def try_hash_approach(words, expected, table_size):
    """
    Try hash table approach where index = hash(letter_set) with quadratic or other probing
    """
    def custom_hash(ls):
        # Try polynomial rolling hash
        h = 0
        for i, c in enumerate(ls):
            h += (ord(c) - ord('a') + 1) * (31 ** i)
        return h
    
    used = {}  # maps index -> letter_set
    results = []
    ls_to_idx = {}
    
    for word in words:
        ls = get_letter_set(word)
        
        if ls in ls_to_idx:
            results.append(ls_to_idx[ls])
        else:
            base_hash = custom_hash(ls)
            idx = base_hash % table_size
            
            # Linear probing
            probe = 0
            while idx in used and used[idx] != ls:
                probe += 1
                idx = (base_hash + probe) % table_size
            
            used[idx] = ls
            ls_to_idx[ls] = idx
            results.append(idx)
    
    return results

# Test with different table sizes
words2 = ["monkey", "frog", "bison", "chinook", "puffin", "rhinoceros"]
expected2 = [0, 1, 2, 3, 4, 6]

print("Testing polynomial hash with different table sizes:")
for size in [7, 10, 20, 50, 100, 1000]:
    result = try_hash_approach(words2, expected2, size)
    match = "✓" if result == expected2 else ""
    print(f"Size {size:4}: {result} {match}")

# Let me also manually check what happens with first letter hash
print("\n" + "="*60)
print("\nTrying simple first-letter based index with offset:\n")

def first_letter_hash(words, expected):
    results = []
    ls_to_idx = {}
    used = set()
    
    for word in words:
        ls = get_letter_set(word)
        
        if ls in ls_to_idx:
            results.append(ls_to_idx[ls])
        else:
            # Index based on position in alphabet of first letter
            base = ord(ls[0]) - ord('a')
            idx = base
            
            # Linear probing if collision
            while idx in used:
                idx += 1
            
            used.add(idx)
            ls_to_idx[ls] = idx
            results.append(idx)
    
    return results

result = first_letter_hash(words2, expected2)
print(f"First letter hash: {result}")
print(f"Expected:          {expected2}")

# Show the first letters
print("\nFirst letters:")
for word in words2:
    ls = get_letter_set(word)
    print(f"{word:15} -> {ls:15} -> first='{ls[0]}' (pos={ord(ls[0])-ord('a')})")
