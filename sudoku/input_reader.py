import numpy as np
import camelot

def create_board(file, outfile):
    df = camelot.read_pdf(file,pages = "all") #address of pdf file
    with open(outfile, "w") as f:
        for i in range(8):
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

if __name__ == '__main__':
    file = 'KD_Sudoku_EZ_8_v1.pdf'
    outfile = 'potato.txt'
    print(read_file(outfile, 8))
    # create_board(file, outfile)