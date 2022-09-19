def rwfile():
    name = "ds.csv"
    with open(name, "r") as infile, open(name.replace("csv", "tsv"), 'w') as outfile:
        for line in infile:
            outfile.write(line.replace('",', '"\t').replace('false,', 'false\t').replace('true,', 'true\t'))

if __name__ == "__main__":
    rwfile()
