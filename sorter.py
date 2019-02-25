import operator
import pdb
from heap_page import HeapPage, PAGE_SIZE_BYTES

def sort(in_filename, out_filename):
    in_file = open(in_filename, 'rb')
    tmp_file = open('sort_temp', 'wb')
    page_count = 0

    hp = HeapPage()

    page_bytes = in_file.read(PAGE_SIZE_BYTES)
    while page_bytes != b'':
        hp.reset()
        hp.read(page_bytes)
        tuples = hp.tuples
        tuples.sort(key = operator.itemgetter(1))
        hp.reset()
        [hp.append(t) for t in tuples]
        tmp_file.write(hp.bytes)
        page_count += 1

        page_bytes = in_file.read(PAGE_SIZE_BYTES)

    in_file.close()
    tmp_file.close()

    print(f"wrote {page_count} individually sorted pages")

    itr = 0
    chunk_size_in_pages = 1
    in_filename = 'sort_temp'
    base_out_filename = out_filename

    while chunk_size_in_pages < page_count:

        print(f"starting iteration with chunk size {chunk_size_in_pages}")
        itr += 1
        in_file = open(in_filename, 'rb')
        out_filename = base_out_filename + '.' + str(itr)
        out_file = open(out_filename, 'wb')

        output_page_buffer = HeapPage()

        left_page_pos = 0
        right_page_pos = chunk_size_in_pages

        while left_page_pos < page_count:

            print(f"loading {chunk_size_in_pages} left pages at {left_page_pos}")
            print(f"loading {chunk_size_in_pages} right pages at {right_page_pos}")
            left_tpls = TuplePuller(in_file, left_page_pos, chunk_size_in_pages)
            right_tpls = TuplePuller(in_file, right_page_pos, chunk_size_in_pages)

            left = left_tpls.next_tpl()
            right = right_tpls.next_tpl()

            while True:
                if left is None:
                    while right is not None:
                        do_append(output_page_buffer, right, out_file)
                        right = right_tpls.next_tpl()
                    break

                elif right is None:
                    while left is not None:
                        do_append(output_page_buffer, left, out_file)
                        left = left_tpls.next_tpl()
                    break

                if left[1] < right[1]:
                    do_append(output_page_buffer, left, out_file)
                    left = left_tpls.next_tpl()
                else:
                    do_append(output_page_buffer, right, out_file)
                    right = right_tpls.next_tpl()


            flush(output_page_buffer, out_file)
            left_page_pos = right_page_pos + chunk_size_in_pages
            right_page_pos = left_page_pos + chunk_size_in_pages

        chunk_size_in_pages = chunk_size_in_pages * 2
        in_filename = out_filename
        in_file.close()
        out_file.close()

def do_append(buf, tpl, out_file):
    if not buf.append(tpl):
        flush(buf, out_file)
        buf.append(tpl)
    print(f"appended: {tpl}")

def flush(buf, out_file):
    print("flushing")
    if len(buf.tuples) > 0:
        out_file.write(buf.bytes)
        buf.reset()


class TuplePuller:
    def __init__(self, in_file, page_start, chunk_size):
        self.in_file = in_file
        self.page_start = page_start
        self.chunk_size = chunk_size
        self.next_page = page_start
        self.page_buffer = HeapPage()
        self.tpl_idx = 0

    def next_tpl(self):
        if self.tpl_idx < len(self.page_buffer.tuples):
            result = self.page_buffer.tuples[self.tpl_idx]
            self.tpl_idx += 1
            return result

        elif self.next_page < self.page_start + self.chunk_size:
            print(f"loading page {self.next_page}, page start: {self.page_start}, chunk size:{self.chunk_size}")
            self.in_file.seek(self.next_page * PAGE_SIZE_BYTES)
            self.next_page += 1
            page_bytes = self.in_file.read(PAGE_SIZE_BYTES)
            if page_bytes == b'':
                return None
            self.page_buffer.reset()
            self.page_buffer.read(page_bytes)
            print("loaded tuples:")
            [print(t) for t in self.page_buffer.tuples]

            self.tpl_idx = 0
            result = self.page_buffer.tuples[self.tpl_idx]
            self.tpl_idx += 1
            return result

        else:
            return None


if __name__ == '__main__':
    # sort('data/movies.dc', 'data/movies_sorted.dc')

    tp = TuplePuller(open('data/movies_sorted.dc.11', 'rb'), 0, 1600)
    tpl1 = tp.next_tpl()
    tpl2 = tp.next_tpl()

    while tpl2 is not None:
        if tpl1[1] > tpl2[1]:
            print(f"out of order: {tpl1[1]}, {tpl2[1]}")

        tpl1 = tpl2
        tpl2 = tp.next_tpl()

