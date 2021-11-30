import os
import gkeepapi
from pathlib import Path


class getAccess:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def replaceForbiddenChar(self, string):
        return string.replace("/", " forward slash").replace("?", " question mark").replace("*", " asterisk").replace(">", " greater").replace("<", " less than").replace(":", " divide").replace("\\", " backslash").replace("\"", " quote").replace("|", " pipe").replace(",", "")

    def connectToKeep(self):
        keep = gkeepapi.Keep()
        keep.login(self.username, self.password)

        note = keep.all()

        if os.path.isdir("notes"):
            print("Directory already exists")
        else:
            path = Path("notes")
            path.mkdir()

        for index in note:
            fileContent = index.text.encode("utf8")
            
            if index.title == "":
                lines = index.text.splitlines()

                if lines:
                    firstLine = lines[0]

                    if firstLine == "" or firstLine == None or firstLine == " ":
                        lines[2] = self.replaceForbiddenChar(lines[2])

                        if os.path.isfile(fileName):
                            print("File already exists")
                            continue
                        else:
                            file = open(fileName, "xb")
                            file.write(fileContent)
                    else:
                        firstLine = self.replaceForbiddenChar(firstLine)

                        if len(firstLine) > 30:
                            fileName = f"notes/{firstLine[0:19]}.txt"

                            if os.path.isfile(fileName):
                                print("File already exists")
                                continue
                            else:
                                file = open(fileName, "xb")
                                file.write(fileContent)
                        else:
                            fileName = f"notes/{firstLine}.txt"

                            if os.path.isfile(fileName):
                                print("File already exists")
                                continue
                            else:
                                file = open(fileName, "xb")
                                file.write(fileContent)
                else:
                    continue
            else:
                index.title = self.replaceForbiddenChar(index.title)

                fileName = f"notes/{index.title}.txt"

                if os.path.isfile(fileName):
                    print("File already exists")
                    continue
                else:
                    file = open(fileName, "xb")
                    file.write(fileContent)


print("This app allows to get your notes from Google Keep and write them to \".txt\" files")
username = input("Your e-mail: ")
password = input("\nYour password: ")
getAccess(username, password).connectToKeep()