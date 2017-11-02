import os, random

os.chdir("/home/data/plants")

classes = os.listdir(".")

if not os.path.exists("test"):
    os.makedirs("test")
if not os.path.exists("train"):
    os.makedirs("train")

for classname in classes:
    if not os.path.exists("test/"+classname):
        os.makedirs("test/"+classname)
    if not os.path.exists("train/"+classname):
        os.makedirs("train/"+classname)

    files = os.listdir(classname)
    n = len(files)

    for f in files:
        if random.random() < 0.3:
            os.rename(classname+"/"+f,"test/"+classname+"/"+f)
        else:
            os.rename(classname+"/"+f,"train/"+classname+"/"+f)



