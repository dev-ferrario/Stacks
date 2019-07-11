#This is a change being made for a pull request

class Stack:
    def __init__(self):
        self.items = []
        self.maxVal = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)
        if not self.maxVal or data >= self.maxVal[len(self.maxVal) - 1]:
            self.maxVal.append(data)

    def pop(self):
        poppedVal = self.items.pop()
        if poppedVal == self.maxVal[len(self.maxVal)-1]:
            self.maxVal.pop()
        return poppedVal

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

    def reverse3(self):
        lo = 0
        hi = len(self.items) - 1
        while lo < hi:
            self.items[lo], self.items[hi] = self.items[hi], self.items[lo]
            lo += 1
            hi -= 1

    def getMax(self):
        if self.maxVal:
            return self.maxVal[len(self.maxVal) - 1]

    def print(self):
        print(self.items)


