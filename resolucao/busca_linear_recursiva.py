def binarysearch(self, value):
    low = self[0];
    high = self[self.size - 1]
    mid = low + high // 2
    if(mid == value):
        return mid
