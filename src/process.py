'''
process.py collects all FEN strings iff a valid game result is next to it (i.e. 1-0 or 0-1 or 1/2-1/2)
In other words, only one FEN string is collected for each game (that is the FEN
which corresponds to the final position)

The output of process.py is a CSV file containing the matches from the regular expression.
'''

filename = raw_input("Enter the filename of the dataset: ")

# file format of f before manipulation should be :
'''
{ rnbqkbnr/pppppppp/8/8/1P6/8/P1PPPPPP/RNBQKBNR b KQkq b3 0 1 } *
Inside the {} is the FEN string. Seperated by one space is the final result of the game.
'''

f = open(filename).read()

import re
regex = r'(\{(.*?)\}\ ((1\-0)|(0\-1)|(1\/2\-1\/2)))'
matches = re.finditer(regex, f, re.M|re.I)

import csv
outfilename = "processed-output.csv"
outfile = open(outfilename, "wb")

for matchNum, match in enumerate(matches):
    for groupNum in range(0, len(match.groups())):
        # delete the {\s from the matched string, then split on {
        fen, result = (match.group(1))[2:].split('}')[:2]
        outfile.write(fen.replace('"', '') + "," + result + "\r\n")
        print(fen.replace('"', '') + "," + result + "\r\n")
