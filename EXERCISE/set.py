# Create a set
alphabet = {"a", "b", "c", "d"}

# Add an element to the set
alphabet.add("e")

# Remove an element from the set
alphabet.remove("a")

# Check if an element is in the set
contains_b = "b" in alphabet
contains_o = "o" in alphabet

# Iterate through the set
print("Alphabet:")
for i in alphabet:
    print(i)

# Create another set
citrus_alphabet= {"f", "g", "e"}
print("Citrus Alphabet:")
for i in citrus_alphabet:
    print(i)

# Perform set operations
union_alphabet_citrus = alphabet.union(citrus_alphabet)
intersection_alphabet_citrus = alphabet.intersection(citrus_alphabet)
difference_alphabet_citrus = alphabet.difference(citrus_alphabet)

# Print the results
print("Contains b? ", contains_b)
print("Contains o? ", contains_o)
print("Union of alphabet and citrus alphabet:", union_alphabet_citrus)
print("Intersection of alphabet and citrus alphabet:", intersection_alphabet_citrus)
print("Difference between alphabet and citrus alphabet:", difference_alphabet_citrus)