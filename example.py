from YourCombinations import YourCombinations

# create YourCombinations
your_combinations = YourCombinations([1, 2, 3])

# power set
print("Power set:")
for i in your_combinations.powerSet():
    print(i)

# combinations with repetition
print("Combinations size 2 with repetition:")
for i in your_combinations.combinations(2, True):
    print(i)

# combinations without repetition
print("Combinations size 2 without repetition:")
for i in your_combinations.combinations(2):
    print(i)

# permutations with repetition
print("Permutations size 2 with repetition:")
for i in your_combinations.permutations(2, True):
    print(i)

# permutations without repetition
print("Permutations size 2 without repetition:")
for i in your_combinations.permutations(2):
    print(i)

##################################################################################

# power set
print("Power set:", list(your_combinations.powerSet()))

# combinations with repetition
print("Combinations with repetition:", list(your_combinations.combinations(2, True)))

# combinations without repetition
print("Combinations without repetition:", list(your_combinations.combinations(2)))

# permutations with repetition
print("Permutations with repetition:", list(your_combinations.permutations(2, True)))

# permutations without repetition
print("Permutations without repetition:", list(your_combinations.permutations(2)))
