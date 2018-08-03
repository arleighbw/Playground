import os

hitDirFileName = ""
hitLineContent = ""

#READFILE
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
fileName = os.path.join(THIS_FOLDER, "SEARCH_SortName.txt")

with open(fileName, "r") as fileIn:
    data = [line.rstrip() for line in fileIn]


#PARSEFILE, write out to CSV
fileOutName = os.path.join(THIS_FOLDER, "ParseResults.csv")

with open(fileOutName,"w") as fileOut:
    outLine = ""
    bHeader = True

    for line in data:

        #header
        if (bHeader): 
            print(line)
            fileOut.write(line + "\n")
            bHeader = False

        if ("C:" in line):
            # print and reset
            if (hitDirFileName):
                outLine = hitDirFileName

                # if displayed
                outLine += ","
                # if report
                outLine += ","
                if (".rpt" in hitDirFileName.lower()):
                    outLine += "X"
                # if extracted, packages?
                outLine += ","
                if (".pkg" in hitDirFileName.lower()):
                    outLine += "X"
                # content
                outLine += "," + hitLineContent
                # filename, displayed, report, extracted
                fileOut.write(outLine + "\n")
            
            hitDirFileName = ""
            hitLineContent = ""

            # new line
            hitDirFileName = os.path.basename(line)
        elif ("Line " in line): 
            hitLineContent = hitLineContent + line + ","

exit()
