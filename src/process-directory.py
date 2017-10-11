import re
import glob

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
                outputfile.write(position[1:].replace('"', '') + "," + whosmove + "," + result.strip() + "\r\n")
                print(position[1:].replace('"','') + "," + whosmove + "," + result.strip() + "\r\n")

# returns row vector corresponding to fen parameter
def vectorize_stripped_fen(fen):
    rows = fen.split('/')
    for row in rows:
        expanded_row = []
        character_list = list(row)
        for character in character_list:
            if character.isdigit():
                for i in range(int(character)):
                    expanded_row[i] = 0 # for the character amount, set that many squares to empty
            else:
