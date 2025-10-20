#!/usr/bin/env python3

def get_letter_set(word):
    return ''.join(sorted(set(word.lower())))

def hash_function(letter_set, method="sum"):
    """Try different hash methods"""
    if method == "sum":
        return sum(ord(c) - ord('a') for c in letter_set)
    elif method == "len":
        return len(letter_set)
    elif method == "product":
        p = 1
        for c in letter_set:
            p *= (ord(c) - ord('a') + 1)
        return p
    elif method == "first":
        return ord(letter_set[0]) - ord('a')
    elif method == "xor":
        x = 0
        for c in letter_set:
            x ^= (ord(c) - ord('a'))
        return x

def test_hash_with_modulo(words, expected, hash_method, modulo):
    """Test if a hash function with modulo and linear probing works"""
    used = set()
    results = []
    letter_sets = {}
    
    for word in words:
        ls = get_letter_set(word)
        
        if ls in letter_sets:
            results.append(letter_sets[ls])
        else:
            h = hash_function(ls, hash_method) % modulo
            
            # Linear probing
            while h in used:
                h += 1
            
            used.add(h)
            letter_sets[ls] = h
            results.append(h)
    
    return results

# Test example 2
words2 = ["monkey", "frog", "bison", "chinook", "puffin", "rhinoceros"]
expected2 = [0, 1, 2, 3, 4, 6]

print("Testing different hash functions with Example 2:")
print(f"Expected: {expected2}\n")

methods = ["sum", "len", "product", "first", "xor"]
modulos = [7, 10, 20, 50, 100]

for method in methods:
    for mod in modulos:
        result = test_hash_with_modulo(words2, expected2, method, mod)
        if result == expected2:
            print(f"✓ MATCH! Method={method}, Modulo={mod}: {result}")

# Let's also check what the hashes are for each word
print("\n" + "="*60)
print("\nDetailed hash values for Example 2:\n")
for word in words2:
    ls = get_letter_set(word)
    print(f"{word:15} ({ls:15}):")
    for method in methods:
        h = hash_function(ls, method)
        print(f"  {method:8}: {h:6} (mod 7={h%7:3}, mod 10={h%10:3})")
