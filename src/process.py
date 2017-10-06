'''
process.py collects all FEN strings iff the game result is next to it
In other words, only one FEN string is collected for each game (that is the FEN
which corresponds to the final position)

The output of process.py is a text file containing the matches from the regular expression.
'''

filename = raw_input("Enter the filename of the dataset: ")

# file format of f before manipulation should be :
'''
{ rnbqkbnr/pppppppp/8/8/1P6/8/P1PPPPPP/RNBQKBNR b KQkq b3 0 1 } *

Inside the {} is the FEN string. Seperated by one space is the final result of the game.
'''
f = open(filename)
outfilename = filename + "_processed.txt"
outfile = open(outfilename, "w")

import re, time
regex = r'(\{(.*?)\}\ ((1\-0)|(0\-1)|(1\/2\-1\/2)))'
matches = re.finditer(regex, f, re.M|re.I)

start = time.time()
for matchNum, match in enumerate(matches):
    print(matchNum)
    for groupNum in range(0, len(match.groups())):
        outfile.write(match.group(1) + "\n")
end = time.time()
print("Completed in " + str(end-start) + " seconds")
