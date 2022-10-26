# Your Combinations Python

An efficient combinatorics Python software to generate and get the list of all **Permutations** and **Combinations** with the ability to enable or disable repetition. (utilizing generators)

## Functions

- [PowerSet](#powerset)
- [Permutation with repetition](#permutation-with-repetition)
- [Permutation without repetition](#permutation-without-repetition)
- [Combinations with repetition](#combinations-with-repetition)
- [Combinations without repetition](#combinations-without-repetition)


## Usage

### PowerSet

```python
your_combinations = YourCombinations([1, 2, 3])
print("Power set:")
for i in your_combinations.powerSet():
    print(i)

// [
//   [],       [ 1 ],
//   [ 2 ],    [ 1, 2 ],
//   [ 3 ],    [ 1, 3 ],
//   [ 2, 3 ], [ 1, 2, 3 ]
// ]
```

### Permutation with repetition

```python
your_combinations = YourCombinations([1, 2, 3])
print("Combinations size 4 with repetition:")
for i in your_combinations.permutations(4, True):
    print(i)

// [ 1, 1, 1, 1 ]
// [ 1, 1, 1, 2 ]
// [ 1, 1, 1, 3 ]
// [ 1, 1, 2, 1 ]
// [ 1, 1, 2, 2 ]
// [ 1, 1, 2, 3 ]
// [ 1, 1, 3, 1 ]
// [ 1, 1, 3, 2 ]
// [ 1, 1, 3, 3 ]
// [ 1, 2, 1, 1 ]
// [ 1, 2, 1, 2 ]
// [ 1, 2, 1, 3 ]
// [ 1, 2, 2, 1 ]
// [ 1, 2, 2, 2 ]
// [ 1, 2, 2, 3 ]
// [ 1, 2, 3, 1 ]
// [ 1, 2, 3, 2 ]
// [ 1, 2, 3, 3 ]
// [ 1, 3, 1, 1 ]
// [ 1, 3, 1, 2 ]
// [ 1, 3, 1, 3 ]
// [ 1, 3, 2, 1 ]
// [ 1, 3, 2, 2 ]
// [ 1, 3, 2, 3 ]
// [ 1, 3, 3, 1 ]
// [ 1, 3, 3, 2 ]
// [ 1, 3, 3, 3 ]
// [ 2, 1, 1, 1 ]
// [ 2, 1, 1, 2 ]
// [ 2, 1, 1, 3 ]
// [ 2, 1, 2, 1 ]
// [ 2, 1, 2, 2 ]
// [ 2, 1, 2, 3 ]
// [ 2, 1, 3, 1 ]
// [ 2, 1, 3, 2 ]
// [ 2, 1, 3, 3 ]
// [ 2, 2, 1, 1 ]
// [ 2, 2, 1, 2 ]
// [ 2, 2, 1, 3 ]
// [ 2, 2, 2, 1 ]
// [ 2, 2, 2, 2 ]
// [ 2, 2, 2, 3 ]
// [ 2, 2, 3, 1 ]
// [ 2, 2, 3, 2 ]
// [ 2, 2, 3, 3 ]
// [ 2, 3, 1, 1 ]
// [ 2, 3, 1, 2 ]
// [ 2, 3, 1, 3 ]
// [ 2, 3, 2, 1 ]
// [ 2, 3, 2, 2 ]
// [ 2, 3, 2, 3 ]
// [ 2, 3, 3, 1 ]
// [ 2, 3, 3, 2 ]
// [ 2, 3, 3, 3 ]
// [ 3, 1, 1, 1 ]
// [ 3, 1, 1, 2 ]
// [ 3, 1, 1, 3 ]
// [ 3, 1, 2, 1 ]
// [ 3, 1, 2, 2 ]
// [ 3, 1, 2, 3 ]
// [ 3, 1, 3, 1 ]
// [ 3, 1, 3, 2 ]
// [ 3, 1, 3, 3 ]
// [ 3, 2, 1, 1 ]
// [ 3, 2, 1, 2 ]
// [ 3, 2, 1, 3 ]
// [ 3, 2, 2, 1 ]
// [ 3, 2, 2, 2 ]
// [ 3, 2, 2, 3 ]
// [ 3, 2, 3, 1 ]
// [ 3, 2, 3, 2 ]
// [ 3, 2, 3, 3 ]
// [ 3, 3, 1, 1 ]
// [ 3, 3, 1, 2 ]
// [ 3, 3, 1, 3 ]
// [ 3, 3, 2, 1 ]
// [ 3, 3, 2, 2 ]
// [ 3, 3, 2, 3 ]
// [ 3, 3, 3, 1 ]
// [ 3, 3, 3, 2 ]
// [ 3, 3, 3, 3 ]
```

### Permutation without repetition

```python
your_combinations = YourCombinations([1, 2, 3])
print("Combinations size 2 without repetition:")
for i in your_combinations.permutations(4, False):
    print(i)

// [ 1, 2 ]
// [ 1, 3 ]
// [ 2, 1 ]
// [ 2, 3 ]
// [ 3, 1 ]
// [ 3, 2 ]
```

### Combinations with repetition

```python
your_combinations = YourCombinations([1, 2, 3])
print("Permutations size 2 with repetition:")
for i in your_combinations.permutations(2, True):
    print(i)

// [ 1, 1, 1, 1 ]
// [ 1, 1, 1, 2 ]
// [ 1, 1, 1, 3 ]
// [ 1, 1, 2, 2 ]
// [ 1, 1, 2, 3 ]
// [ 1, 1, 3, 3 ]
// [ 1, 2, 2, 2 ]
// [ 1, 2, 2, 3 ]
// [ 1, 2, 3, 3 ]
// [ 1, 3, 3, 3 ]
// [ 2, 2, 2, 2 ]
// [ 2, 2, 2, 3 ]
// [ 2, 2, 3, 3 ]
// [ 2, 3, 3, 3 ]
// [ 3, 3, 3, 3 ]
```

### Combinations without repetition

```python
your_combinations = YourCombinations([1, 2, 3])
print("Permutations size 2 without repetition:")
for i in your_combinations.permutations(2, False):
    print(i)

// [ 1, 2 ]
// [ 1, 3 ]
// [ 2, 3 ]
```

© Copyright, 2022 Max Base
