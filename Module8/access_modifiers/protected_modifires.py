class Square:
    def __init__(self):
        self._length = "This variable is with length 5"

    def _area(self):
        return self._length * self._length

square = Square()
print(square._length)