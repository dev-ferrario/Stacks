#This is a change being made for a pull request

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def reverse1(self):
        result = self.items.copy()
        lo = 0
        hi = len(self.items) - 1
        while lo < hi:
            result[lo], result[hi] = result[hi], result[lo]
            lo += 1
            hi -= 1
        return result

    def reverse2(self):
        result = self.items.copy()
        result.reverse()
        return result

    def print(self):
        print(self.items)

