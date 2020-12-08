import tempfile
import os.path
import uuid


class File:
    def __init__(self, path):
        self.path = os.path.join(tempfile.gettempdir(), path)
        if not os.path.isfile(self.path):
            open(self.path, 'w').close()
        self.current_position = 0

    def read(self):
        with open(self.path, 'r') as file:
            f = file.read()
            return f

    def write(self, srting):
        with open(self.path, 'w') as file:
            file.write(srting)
            print(len(srting))

    def __add__(self, other):
        sum_file = os.path.join(tempfile.gettempdir(), str(uuid.uuid1()))
        new = type(self)(sum_file)
        new.write((self.read() + other.read()))
        return new

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as file:
            file.seek(self.current_position)
            lines = file.readline()
            self.len_file = len(lines)
            if not lines:
                self.current_position = 0
                raise StopIteration
            self.current_position = file.tell()
            return lines
