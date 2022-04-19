import os

# Replace appropriate folder name
myFolder = "Train_voc"
files = os.listdir(myFolder)

# Gathering just the xml files from specified folder
xml_files = [x for x in files if x[-4:] == ".xml"]

# Writes paths.txt, with each line being the XML file path
with open('paths.txt', 'w') as filehandle:
    for listitem in xml_files:
        filehandle.write(f'./{myFolder}/%s\n' % listitem)