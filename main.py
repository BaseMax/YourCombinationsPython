from YourCombinations import YourCombinations

# create YourCombinations
your_combinations = YourCombinations([1, 2, 3])

# power set
for i in your_combinations.powerSet([1, 2, 3]):
    print(i)

# combinations with repetition
for i in your_combinations.combinations(2, True):
    print(i)

# combinations without repetition
for i in your_combinations.combinations(2):
    print(i)

# permutations with repetition
for i in your_combinations.permutations(2, True):
    print(i)

# permutations without repetition
for i in your_combinations.permutations(2):
    print(i)

