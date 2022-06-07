from tkinter import *
from tkinter import filedialog
import re

root = Tk()
root.title("Fehler finder")

def openFile():
    file = filedialog.askopenfilename(initialdir='/',title="Laden Sie Log Datei hoch")
    
    content_file = open(file).read()
    return content_file

def find_fehlers(logfile_content):
    fehlers = []
    finded_CCU = 0
    finded_BMU = 0
    finded_EGS = 0
    finded_DME = 0
    finded_INV = 0
    finded_EPK_Pr = 0
    for match in re.finditer(r"does not match",logfile_content):
        if re.findall(r"CCU", logfile_content[match.start()-100:match.start()]):
            if finded_CCU == 0:
                fehlers.append("CCU A2L Version stimmt nicht überein ")
                finded_CCU = 1
        if re.findall(r"BMU", logfile_content[match.start()-100:match.start()]):
            if finded_BMU == 0:
                fehlers.append("BMU A2L Version stimmt nicht überein ")
                finded_BMU = 1
        if re.findall(r"CPP ", logfile_content[match.start()-100:match.start()]) | re.findall(r"EGS", logfile_content[match.start()-100:match.start()]):
            if finded_EGS == 0:
                fehlers.append("EGS A2L Version stimmt nicht überein ")
                finded_EGS = 1
        if re.findall(r"_default_ModuleName ", logfile_content[match.start()-100:match.start()])| re.findall(r"DME", logfile_content[match.start()-100:match.start()]):
            if finded_DME == 0:
                fehlers.append("DME A2L Version stimmt nicht überein ")
                finded_DME = 1
        if re.findall(r"INV", logfile_content[match.start()-100:match.start()]):
            if finded_INV == 0:
                fehlers.append("INV A2L Version stimmt nicht überein ")
                finded_INV = 1
    for match in re.finditer(r"INV returned error code 0x24",logfile_content):
        if finded_EPK_Pr == 0:
            fehlers.append("INV EPK Prüfung muss deaktiviert werden")
            finded_EPK_Pr = 1
    return fehlers    

                
content_file = openFile()
fehlers = find_fehlers(content_file)


textEditor = Text(root,width=60,height=20,wrap=WORD)
textEditor.pack()
for fehler in fehlers:
    textEditor.insert("end",f"{fehler}\n")


root.geometry("500x400+400+100")
root.mainloop()
