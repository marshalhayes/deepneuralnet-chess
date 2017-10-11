import re
import csv
import glob

regex = r'(\{(.*?)\}\ ((1\-0)|(0\-1)|(1\/2\-1\/2)))'
outputfile = open('processed-output-fen_and_result.csv','wb')
outputfile.write("position, color_to_move, result")

matchcount = 0
for filename in glob.glob('*.txt'):
    print('######################################')
    print(filename + " starting to be read")
    print('######################################')
    with open(filename) as f:
        print("Going through each line of " + filename)
        for line in f:
            match = re.search(regex, line)
            if match is not None:
                matchcount += 1
                fen, result = match.group(0)[2:].split('}')[:2]
                position, whosmove = fen.split(' ')[:2].replace('"','')
                outputfile.write(position[1:] + "," + whosmove + "," + result.strip() + "\r\n")
                print(position[1:] + "," + whosmove + "," + result + "\r\n")
