#!/usr/bin/env python3

def get_letter_set(word):
    return ''.join(sorted(set(word.lower())))

# All examples combined
examples = [
    (["ieeextreme", "one", "brainteaser", "snow", "unicorn", "laparoscopy", 
      "overcautiousness", "cosmos", "conclusion", "wisconsin", "binationalism",
      "barbascos", "cacophonic", "inosculate", "pneumonoconiosis"],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 48]),
    (["monkey", "frog", "bison", "chinook", "puffin", "rhinoceros"],
     [0, 1, 2, 3, 4, 6]),
    (["kale", "asparagus", "broccoli", "spinach", "chocolate"],
     [0, 1, 2, 3, 4])
]

# Collect all unique letter sets with their outputs
unique_sets = {}
for words, outputs in examples:
    for word, output in zip(words, outputs):
        ls = get_letter_set(word)
        if ls not in unique_sets:
            unique_sets[ls] = (output, word)

# Sort by output
sorted_sets = sorted(unique_sets.items(), key=lambda x: x[1][0])

print("All UNIQUE letter sets sorted by output:\n")
print(f"{'Index':<6} {'Letters':<20} {'Example Word':<20}")
print("="*50)
for ls, (idx, word) in sorted_sets:
    print(f"{idx:<6} {ls:<20} {word:<20}")

print("\n" + "="*60)
print("\nLooking for the pattern...")
print("\nNotice: Most are sequential (0-13), but then jumps:")
print("  - Index 5 skipped in example 2? NO - it exists")
print("  - Index 14 missing, jumps to 48")
print("  - In example 2, we have 0,1,2,3,4,6 (5 is missing)")

print("\nLet me check if rhinoceros/puffin share letters:")
rhino = get_letter_set("rhinoceros")
puff = get_letter_set("puffin")
print(f"rhinoceros: {rhino}")
print(f"puffin: {puff}")
print(f"Common letters: {set(rhino) & set(puff)}")
