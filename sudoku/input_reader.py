import os

import numpy as np
import camelot

def create_board(file, outfile, has_blank = False):
    df = camelot.read_pdf(file ,pages = "all") #address of pdf file
    with open(outfile, "w") as f:
        iter = []
        if has_blank:
            iter = range(0, 16, 2)
        else:
            iter = range(0, 8)
        for i in iter:
            if has_blank:
                f.write(f'Board no #{i // 2}\n')
            else:
                f.write(f'Board no #{i}\n')

            for j in range(9):
                for k in range(9):
                    if not df[i].df[j][k]:
                        df[i].df[j][k] = '0'
                    f.write(df[i].df[j][k] + ' ')
                f.write('\n')

def read_file(file, number):
    matrixes = []
    with open(file) as f:
        for _ in range(number):
            matrix = []
            line = f.readline()
            for i in range(9):
                line = f.readline().strip().split()
                matrix.append(line)
            matrixes.append(matrix)

    return matrixes

def generate_data(directory):
    for x in os.listdir(directory):
        if not ('ST' in x or 'TF' in x or 'IN' in x) or not (".pdf" in x):
            continue
        print(x)
        has_blank = False
        if ('ST' in x or 'TF' in x or 'IN' in x):
            has_blank = True
        newDir = x[:-4] + ".txt"
        create_board(directory + r'/' + x, directory + r'/' + newDir, has_blank)

if __name__ == '__main__':
    directory = 'input_data'
    generate_data(directory)
