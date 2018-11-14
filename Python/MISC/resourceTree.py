import fileNode as fileNode
import os

class resourceTree():

    def __init__(self, root):
        self.root = root
        self.appPath = []
        self.populateAppPath();
        self.resourceDict = {}


    def setWorkingDirectory(self, workDir):
        if (os.path.isdir(workDir)):
            os.chdir(workDir)

    def populateAppPath(self):
        initFile = os.path.join(os.getcwd(),"resourceTree.ini")
        if (os.path.exists(initFile)):
            with open(initFile,"r") as file:
                data = file.readlines()

                for line in data:
                    param = line.split("=")
                    if ("APPPATH" == param[0].upper()):
                        dirs = param[1].split(";")
                        for appDir in dirs:
                            self.appPath.append(appDir)
                    if ("HOMEPATH" == param[0].upper()):
                        self.appPath.append(param[1].rstrip('\n'))

    def findFile(fileName):
        

    def populateResourceTree(self, root, filePath):
        if not (root): 
            return

        with open(os.path.join(filePath,root)) as srcFile:
            data = srcFile.readlines()

            for line in data:
                code = split(" ")
                if ["USE" == code.trim().upper()]:
                    tgtFildFullPath = findFile(root)






root = fileNode("root.src", os.getcwd())
rt = resourceTree(root)
print(rt.appPath)