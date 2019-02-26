import pdb
import csv
from functools import reduce
from io import StringIO

PAGE_SIZE_BYTES = 2**13

class HeapPage:

    def __init__(self, max_tpl_count):
        self.reset()
        self.max_tpl_count = max_tpl_count

    def reset(self):
        self.ptr_offset = 0
        self.tpl_offset = PAGE_SIZE_BYTES

        self.tuples = []
        self.bytes = bytearray(PAGE_SIZE_BYTES)

    def read(self, inp):
        i = 0
        ptr = int.from_bytes(inp[ i:i+2 ], byteorder='big')
        tlen = int.from_bytes(inp[ i+2 : i+4 ], byteorder='big')

        while ptr != 0:
            raw_tup = inp[ ptr : ptr+tlen ]
            raw_csv = raw_tup.decode('utf-8')
            inp_io = StringIO(raw_csv)
            reader = csv.reader(inp_io)
            tpl = tuple(next(reader))
            self.tuples.append(tpl)

            i += 4
            ptr = int.from_bytes(inp[ i:i+2 ], byteorder='big')
            tlen = int.from_bytes(inp[ i+2 : i+4 ], byteorder='big')

        self.bytes = inp

    def append(self, tpl):
            if len(self.tuples) >= self.max_tpl_count:
                return False

            output = StringIO()
            writer = csv.writer(output)
            writer.writerow(list(tpl))
            tpl_string = output.getvalue().strip()

            tpl_bytes = bytearray(tpl_string, 'utf-8')
            tpl_bytes_len = len(tpl_bytes)

            new_ptr_offset = self.ptr_offset + 4
            new_tpl_offset = self.tpl_offset - tpl_bytes_len

            self.tpl_offset = new_tpl_offset

            self.bytes[self.ptr_offset : self.ptr_offset + 2] = self.tpl_offset.to_bytes(2, byteorder='big')
            self.bytes[self.ptr_offset + 2 : self.ptr_offset + 4] = tpl_bytes_len.to_bytes(2, byteorder='big')
            self.bytes[self.tpl_offset : self.tpl_offset + tpl_bytes_len] = tpl_bytes
            self.tuples.append(tuple)

            self.ptr_offset = new_ptr_offset
            return True

if __name__ == '__main__':
    hp = HeapPage()
    hp.append((1,2))
    hp.append((4,5))
    print(hp.bytes)

