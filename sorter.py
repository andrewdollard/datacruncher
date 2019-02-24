import operator
from heap_page import HeapPage, PAGE_SIZE_BYTES

def sort(in_filename, out_filename):
    in_file = open(in_filename, 'rb')
    out_file = open(out_filename, 'wb')

    hp = HeapPage()

    page_bytes = in_file.read(PAGE_SIZE_BYTES)
    while page_bytes != b'':
        hp.read(page_bytes)
        tuples = hp.tuples
        tuples.sort(key = operator.itemgetter(1))
        hp.reset()
        [hp.append(t) for t in tuples]
        out_file.write(hp.bytes)

        page_bytes = in_file.read(PAGE_SIZE_BYTES)

    in_file.close()
    out_file.close()

if __name__ == '__main__':
    sort('data/movies.dc', 'data/movies_sorted.dc')

