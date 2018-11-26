import glob2
from datetime import datetime

fileNames = glob2.glob("file*")

with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", "w") as file:
    for fileName in fileNames:
        with open(fileName, "r") as f:
            file.write(f.read() + "\n")