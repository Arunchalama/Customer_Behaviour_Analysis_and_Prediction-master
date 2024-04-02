import sys

try:
    infile = sys.argv[1]
    tcomp = -1
    with open("company_log.csv", "a") as g:
        with open(infile) as f:
            for line in f:
                fields = line.strip().split()
                if len(fields) >= 5:  # Check if line has at least 5 fields
                    comp = fields[1]
                    if comp != tcomp:
                        tcomp = comp
                        g.write("\n{},{}".format(tcomp, fields[4]))
                    else:
                        g.write(",{}".format(fields[4]))
except IndexError:
    print("Error: Input file does not have the expected format.")
except FileNotFoundError:
    print("Error: Input file not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
