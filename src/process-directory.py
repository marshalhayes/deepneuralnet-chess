import re
import csv
import glob

regex = r'(\{(.*?)\}\ ((1\-0)|(0\-1)|(1\/2\-1\/2)))'
outputfile = open('processed-output-fen_and_result.csv','wb')

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
                outputfile.write(fen.replace('}', "''").replace('"', '').strip() + "," + result.strip() + "\r\n")
                print('Match ' + str(matchcount) + ' found')
