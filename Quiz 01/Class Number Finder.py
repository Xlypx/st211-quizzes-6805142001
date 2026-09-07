class NumFinder:
    def init(self):
        self.smallest = float('inf')
        self.largest = float ('-inf')

    def find(self, nums):
        for n in nums:
            if n < self.smallest:
                self.smallest = n
            elif n > self.largest:
                self.largest = n
nf = NumFinder()
nf.find([4,25,7,9])
print(nf.smallest, nf.largest)
