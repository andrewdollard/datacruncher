from heap_page import HeapPage
import csv
import os

def load(in_filename, out_filename):
    in_file = open(in_filename, 'r')
    out_file = open(out_filename, 'wb')

    hp = HeapPage(36)

    reader = csv.reader(in_file)
    schema = reader.__next__()

    for line in reader:
        tpl = tuple(line)
        if not hp.append(tpl):
            out_file.write(hp.bytes)
            hp.reset()
            hp.append(tpl)

    out_file.write(hp.bytes)
    out_file.close()
    in_file.close()

if __name__ == '__main__':
    load('data/movies.csv', 'data/movies.dc')
    # load('data/ratings.csv', 'data/ratings.dc')


