class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val):
        self.s.append(val)

        if not self.m or val <= self.m[-1]:
            self.m.append(val)

    def pop(self):
        if self.s[-1] == self.m[-1]:
            self.m.pop()

        self.s.pop()

    def top(self):
        return self.s[-1]

    def getMin(self):
        return self.m[-1]