def __size__(self):
    count = -1
    walk = self._header
    while walk != self.trailer:
        count += 1
        walk = walk._next
    return count