
class YourCombinations:
    def __init__(self, elements):
        self.elements = elements

    def powerSet(self, array):
        size = 2 ** len(array)
        
        for i in range(size):
            cur = []
            for j in range(len(array)):
                if (i & (1 << j)) > 0:
                    cur.append(array[j])
            yield cur

    def combinations(self, length, with_repetition = False, position = 0, elements = []):
        size = len(self.elements)
        
        for i in range(position, size):
            elements.append(self.elements[i])

            if len(elements) == length:
                yield elements
            else:
                yield from self.combinations(length, with_repetition, (i + 1) if with_repetition == False else i, elements)
            
            elements.pop()

    def permutations(self, length, with_repetition = False, elements = [], keys = []):
        for key, value in enumerate(self.elements):
            if with_repetition == False:
                if key in keys:
                    continue

            keys.append(key)
            elements.append(value)
            
            if len(elements) == length:
                yield elements
            else:
                yield from self.permutations(length, with_repetition, elements, keys)
            
            keys.pop()
            elements.pop()

