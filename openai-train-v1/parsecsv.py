import csv
import sys
import re

def myclean(value):
    v = ''.join(value.splitlines())
    v = v.replace('"', '')
    return v 

if len(sys.argv)==1:
    print("<input file> <outputfile>")
for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])


f = open(sys.argv[2], "a") 

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        inputstr = ""
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
#           {"prompt": "Coloque el cursor al inicio de la p\u00e1gina en blanco y use la tecla DELETE tantas veces como sea necesario hasta colocar el texto en el lugar deseado.\nEnglish translation:", "completion": " Move the mouse cursor to the beginning of the blank page and press the DELETE key as often as needed until the text is in the desired spot.###"}
            inputstr = ""
            inputstr += "{\"prompt\": "
            inputstr += ("\"")
            inputstr += (myclean(row[1]))
            inputstr +=  (" -->\", ")
            inputstr +=  (" \"completion\": \" ")
            inputstr +=  ("Instruction #1:   ")
            inputstr += (myclean(row[2]))
            inputstr +=  ("   Instruction #2:   ")
            inputstr +=  (myclean(row[3]))
            inputstr += ("   Instruction #3:   ")
            inputstr +=  (myclean(row[4]))
            inputstr += ("   Less Emotion:   ")
            inputstr +=  (myclean(row[5]))
            inputstr +=  ("   More Emotion:   ")
            inputstr +=  (myclean(row[6]))
            inputstr += ("    Happiness Domain:   ")
            inputstr += (myclean(row[7]))
            inputstr += ("     From Feelings (A):   ")
            inputstr +=  (myclean(row[8]))
            inputstr += ("   North Star (A):   ")
            inputstr += (myclean(row[9]))
            inputstr += ("   Parent Lineage:   ")
            inputstr +=  (myclean(row[10]))
            inputstr +=  ("   From Feelings (Final):   ")
            inputstr +=  (myclean(row[11]))
            inputstr +=  ("   To Feelings (Final):   ")
            inputstr +=  (myclean(row[12]))
            inputstr +=  ("   Specific Lineage:   ")
            inputstr +=  (myclean(row[13]))
            inputstr += ("   Immediate?:   ")
            inputstr +=  (myclean(row[14]))
            inputstr +=  ("   Context:   ")
            inputstr += (myclean(row[15]))
            inputstr +=  ("   END .###\"}\n")
            f.write(inputstr)

            print(inputstr)


            print(len(re.findall(r'\w+', inputstr)))
            inputstr = "" 

        line_count += 1
    print(f'Processed {line_count} lines.')
f.close()

