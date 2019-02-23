import pdb
from functools import reduce

PAGE_SIZE_BYTES = 128

class HeapPage:

    def __init__(self):
        self.tuples = []

    def read(inp):
        i = 0
        ptr = inp[ i : i+1 ]
        len = inp[ i+2 : i+3 ]
        while ptr is not 0:
            raw_tup = inp[ ptr : ptr+len ]
            self.tuples.append(tuple(raw_tup.split(',')))

    def write(self, tuples):
        output = bytearray(PAGE_SIZE_BYTES)

        tuple_strings = [','.join([str(el) for el in t]) for t in tuples]
        total_tuples_bytes = reduce(lambda sum, t: sum + len(t.encode('utf-8')), tuple_strings, 0)

        pointer_offset = 0
        tuple_offset = PAGE_SIZE_BYTES - total_tuples_bytes

        for i in range(len(tuple_strings)):
            output[pointer_offset : pointer_offset + 2] = tuple_offset.to_bytes(2, byteorder='big')
            tuple_length = len(tuple_strings[i].encode('utf-8'))
            output[pointer_offset + 2 : pointer_offset + 4] = tuple_length.to_bytes(2, byteorder='big')

            output[tuple_offset : tuple_offset + tuple_length] = bytearray(tuple_strings[i], 'utf-8')

            pointer_offset += 4
            tuple_offset += tuple_length

        return output

if __name__ == '__main__':
    tuples = [(1,2), (3,4)]
    hp = HeapPage()
    print(hp.write(tuples))

