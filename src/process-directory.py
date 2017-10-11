import re
import csv
import glob

regex = r'(\{(.*?)\}\ ((1\-0)|(0\-1)|(1\/2\-1\/2)))'
outputfile = open('processed-output.csv','wb')

matchcount = 0
for filename in glob.glob('*.pgn'):
    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match is not None:
                matchcount += 1
                fen, result = match.split('}')
                outfile.write(fen.replace('"', None).strip() + "," + result.strip() + "\r\n")
                print('Match' + str(matchcount) + ' found')
