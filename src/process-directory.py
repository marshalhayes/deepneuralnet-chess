import re
import glob

COLS = "a8,b8,c8,d8,e8,f8,g8,h8,a7,b7,c7,d7,e7,f7,g7,h7,a6,b6,c6,d6,e6,f6,g6,h6,a5,b5,c5,d5,e5,f5,g5,h5,a4,b4,c4,d4,e4,f4,g4,a3,b3,c3,d3,e3,f3,g3,h3,a2,b2,c2,d2,e2,f2,g2,h2,a1,b1,c1,d1,e1,f1,g1"
# returns row vector corresponding to row fen string
def vectorize_stripped_fen(fen_row_string):
    row_vector = []
    row_elements = list(fen_row_string)
    for elem in row_elements:
        if elem.isdigit():
            for num in range(int(elem)):
                row_vector.append(0) # if the elem is a number, set that number of preceeding elements to empty squares (0)
        else:
            row_vector.append(elem) # if the elem is a piece (letter)

    return row_vector

regex = r'(\{(.*?)\}\ ((1\-0)|(0\-1)|(1\/2\-1\/2)))'
outputfile = open('processed-output-fen_and_result.csv','wb')
outputfile.write(COLS + "\r\n")

matchcount = 0
for filename in glob.glob('*.txt'):
    print("Reading " + filename + " ... ")
    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match is not None:
                matchcount += 1
                fen, result = match.group(0)[2:].split('}')[:2]
                position, whosmove = fen.split(' ')[:2]

                position = position[1:].replace('"', '')
                rows = position.split('/')

                row_vectors = []
                position_vector = []
                for row in rows:
                    row_vectors = vectorize_stripped_fen(row) + row_vectors

                position_vector = row_vectors

                outputfile.write(",".join(str(x) for x in position_vector + "," + whosmove + "," + result + "\r\n")
                print(str(matchcount) + " matches found");
