import os.path

class FileNode():
    '''
        TODO: may include: 
            directory, current level
        should probly have some functions:
            check if file exists
            need to think about traversal
            should every node have list of children
    '''
    def __init__(self, fileName, filePath):
        self.fileName = fileName
        self.filePath = filePath
        self.fullPath = os.path.join(filePath, fileName)

    def setFilePath(self, filePath):
        self.filePath = filePath
        self.fullPath = os.path.join(self.filePath, self.fileName)


# baseFile = FileNode("startfile.txt")

# baseFile.fileName = "newFile.txt"
# print(baseFile.fileName)
