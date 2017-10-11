import re
import glob

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
outputfile.write("position, color_to_move, result")

matchcount = 0
for filename in glob.glob('*.txt'):
    print('######################################')
    print("Reading " + filename + " ... ")
    print('######################################')
    with open(filename) as f:
        print("Going through each line of " + filename)
        for line in f:
            match = re.search(regex, line)
            if match is not None:
                matchcount += 1
                fen, result = match.group(0)[2:].split('}')[:2]
                position, whosmove = fen.split(' ')[:2]
                # outputfile.write(position[1:].replace('"', '') + "," + whosmove + "," + result.strip() + "\r\n")
                # print(position[1:].replace('"','') + "," + whosmove + "," + result.strip() + "\r\n")
                outputfile.write(",".join(vectorize_stripped_fen(position[1:].replace('"',''))) + "," + whosmove + "," + "\r\n")
                print(str(match) + " matches found");
