class Square:
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def area(self):
        return self.size * self.size
