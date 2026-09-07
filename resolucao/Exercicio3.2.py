def __mid__(self):
    walkfront = self._header
    walkback = self._trailer
    while walkfront != walkback and walkfront.next != walkback:
        walkfront = walkfront._next
        walkback = walkback.__prev
    return walkfront    