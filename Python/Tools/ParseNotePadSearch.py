import os

#targetFile 
# targetVar -includes position ex. body.4
# returns 0 if not targetVar not found
def findCountDFImgVarSize (targetFile, targetVar):
    #clean DF image variable specifics
    targetVar = targetVar.rstrip("&")

    targetPos = int(targetVar[targetVar.rindex(".")+1:])
    targetVar = "/" + targetVar[:targetVar.rindex(".")].upper()
    lImageVars = []

    with open(targetFile, "r") as fileIn:
        fileDat = [line.strip() for line in fileIn]

        for line in fileDat:
            # find targetVar and all its image variables
            if (len(line)):
                if (line[0] == "/"):
                    # Headers could have spacing like /BODY HEADER
                    lImageVarHeader = line.split()
                    currentImgVar = lImageVarHeader[0].upper()
                if (currentImgVar == targetVar):
                    if ("_" in line):
                        #convert weird characters to space, to split on
                        line = line.replace("³"," ")

                        lLineElements = line.split()
                        for elements in lLineElements:
                            if ("_" in elements): 
                                lImageVars.append(elements)
                # NEED TO READ ENTIRE FILE.. can't trust image variables declared prior to comment section
                # break if we hit/pass comment section

                #### actually can run up until the first usage of targetVar

                #if (("/*" in line[:5]) or ("//" in line [:5]) or ("#INCLUDE" in line.upper())):
                #    break

    if (len(lImageVars) >= targetPos):
        # Could have characters other than '_' ex '__/__/__'
        # return len(lImageVars[targetPos-1])
        return (lImageVars[targetPos-1].count('_'))

    return 0

#print(findCountDFImgVarSize("C:\\Data\\CodeQual\\AZ\\Src\\AZ201EAI.RPT","BODY.67"))
#exit()


hitDirFileName = ""
hitLineContent = ""
hitDirLineFull = ""


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

        if ("C:\\" in line):
            # print and reset
            if (hitDirFileName):
                outLine = hitDirFileName
                outLine += ","

                # if DISPLAYED SECTION
                if (".VW" in hitDirFileName.upper()) or (".DP" in hitDirFileName.upper()) or (".DG" in hitDirFileName.upper()) or (".SL" in hitDirFileName.upper()) or (".SV" in hitDirFileName.upper()) or (".PKG" in hitDirFileName.upper()):
                    srcFile = hitDirLineFull[:hitDirLineFull.index(" (")].strip()
                    lContentCodes = hitLineContent.split("||,")
                    lContentCodes = list(filter(None,lContentCodes))

                    for codeLine in lContentCodes:
                        if ("ENTRY_ITEM" in codeLine.upper()):
                            outLine += "ENTRY_ITEM" + "||"
                        elif ("YESNO_BOX" in codeLine.upper()):
                            outLine += "YESNO_BOX" + "||"
                        elif ("STOP_BOX" in codeLine.upper()):
                            outLine += "STOP_BOX" + "||"
                        elif ("FUNCTION_RETURN" in codeLine.upper()):
                            outLine += "FUNCTION_RETURN" + "||"
                        elif ("MOVE" in codeLine.upper()):
                            # continuation character, next entry in search file possibly isn't next line in searchhit file
                            if (codeLine.strip().endswith(";")):
                                outLine += codeLine + "||"
                            else:
                                lCodes = [x.upper() for x in codeLine.split()]
                                outLine += lCodes[lCodes.index("TO") + 1] + "||"


                outLine += ","
                # if SIZE SECTION
                if (".RPT" in hitDirFileName.upper()) or (".INC" in hitDirFileName.upper()):

                    lContentItems = hitLineContent.split("||,")
                    srcFile = hitDirLineFull[:hitDirLineFull.index(" (")].strip()
                    srcImgVar = ""

                    for item in lContentItems:
                        if ("MOVE" in item.upper()) or ("PRINT" in item.upper()):
                            lCodes = [x.upper() for x in item.split()]
                            srcImgVar = lCodes[lCodes.index("TO") + 1]
                            
                            #find image var, otherwise print TO 
                            if ("." in srcImgVar) and (srcImgVar[srcImgVar.rindex(".")+1:].isnumeric()):
                                    print ("findCountDFImgVarSize: " + srcFile + " " + srcImgVar)

                                    ##These files aren't encoded in a unreadable format
                                    if not ("AZ329RA" in srcFile.upper()) and not ("HW523RE" in srcFile.upper()):
                                        outLine += str(findCountDFImgVarSize(srcFile, srcImgVar)) + "||"
                                    print ("findCountDFImgVarSize Result: " + outLine)
                            else:
                                outLine += srcImgVar + "||"
                

                outLine += ","
                # if EXTRACTED SECTION
                if (".VW" in hitDirFileName.upper()) or (".DP" in hitDirFileName.upper()) or (".DG" in hitDirFileName.upper()) or (".SL" in hitDirFileName.upper()) or (".SV" in hitDirFileName.upper()) or (".PKG" in hitDirFileName.upper()):
                    srcFile = hitDirLineFull[:hitDirLineFull.index(" (")].strip()
                    lContentCodes = hitLineContent.split("||,")
                    lContentCodes = list(filter(None,lContentCodes))

                    for codeLine in lContentCodes:
                        if ("SEND" in codeLine.upper()):
                            lCodes = [x.upper() for x in codeLine.split()]
                            outLine += lCodes[lCodes.index("SEND") + 1] + "||"
                        elif ("SET" in codeLine.upper()):
                            # continuation character, next entry in search file possibly isn't next line in searchhit file
                            if (codeLine.strip().endswith(";")):
                                outLine += codeLine + "||"
                            else:
                                lCodes = [x.upper() for x in codeLine.split()]
                                # SET is common, looking for individual key word
                                if (lCodes.count("SET")):
                                    outLine += lCodes[lCodes.index("TO") + 1] + "||"
                        elif ("GET" in codeLine.upper()):
                            # continuation character, next entry in search file possibly isn't next line in searchhit file
                            if (codeLine.strip().endswith(";")):
                                outLine += codeLine + "||"
                            else:
                                lCodes = [x.upper() for x in codeLine.split()]
                                # GET is common, looking for individual key word
                                if (lCodes.count("GET")):
                                    outLine += lCodes[lCodes.index("TO") + 1] + "||"
                        else:
                            outLine += codeLine + "||"


                outLine += ","
                # SEARCH HIT CONTENT SECTION
                outLine += hitLineContent
                # FORMATTED - filename, displayed, report, extracted
                fileOut.write(outLine + "\n")
            
            hitDirFileName = ""
            hitLineContent = ""
            hitDirLineFull = ""
            # new line
            hitDirLineFull = line
            hitDirFileName = os.path.basename(line)
        elif ("Line " in line): 
            hitLineContent += line + "||,"

exit()
