import csv
import sys

print("""
\\documentclass[11pt]{article}
\\usepackage[a4paper, margin=0.5cm]{geometry}
\\usepackage{graphicx}
\\usepackage{array}
\\usepackage{longtable}
\\usepackage[originalparameters]{ragged2e}
\\renewcommand*\\familydefault{\\sfdefault}

\\begin{document}

\\newcolumntype{C}[1]{%
 >{\\vbox to 1ex\\bgroup\\vfill}%
 p{#1}%
 <{\\egroup}} 

\\renewcommand{\\arraystretch}{1.5}
\\setlength{\\tabcolsep}{0.2em}
\\small {
\\begin{longtable}{ @{\\hspace{-.5\\arrayrulewidth}}C{0pt}@{\\hspace{-.5\\arrayrulewidth}}|m{0.3cm}>{\\RaggedRight}p{4cm}|m{0.3cm}>{\\RaggedRight}p{4cm}|m{0.3cm}>{\\RaggedRight}p{4cm}|m{0.3cm}>{\\RaggedRight}p{4cm}| }
\\hline
""")

per_row = 4

row_item = 0

with open(sys.argv[1]) as file:
    items = csv.reader(file, delimiter="\t")
     
    for line in items:
        try:
            count = int(line[0])
        except ValueError:
            count = 0
        date = line[1]
        name = line[2]
        field_no = line[3]
        
        if count > 0 and name:
            for i in range(0, count):
            #if row_item > 0:
                print("&", end=" ")

                if field_no:
                    field_no_str = field_no.replace(" ", "~")
                else:
                    field_no_str = ""

                print ("\\rotatebox[origin=B]{90}{\\scriptsize " + date + "~} & " + name + " " + field_no_str, end="")
                row_item += 1

                if row_item >= per_row:
                    print("\\\\")
                    print("\\hline")
                    row_item = 0

    for i in range(row_item, per_row):
        print("& &", end="")
        
    if row_item > 0:
        print("\\\\")
        print("\\hline")
        

print("""
\\end{longtable}
}
\\end{document}
""")
