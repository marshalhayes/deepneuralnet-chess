outputfile = open("quotes-removed-test.csv", "w")
with open("test-data.csv", "r") as f:
    for line in f:
        x = line.replace('"','')
        outputfile.write(x)
