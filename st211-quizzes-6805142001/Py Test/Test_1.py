class NumFinder:
    def __init__ (self):
        self.smallest = float ('inf') 
        self.largest = float ('-inf') 
    def find (self, nums):
            for n in nums:
                if n < self.smallest:
                    self.smallest = n
                elif n > self.largest:
                        self.largest = n
nf = NumFinder()
nf.find ([4, 3, 2, 1])
print(nf.largest) 
print(nf.smallest)
