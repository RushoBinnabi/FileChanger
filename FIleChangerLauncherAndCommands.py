from tkinter.filedialog import askdirectory
import os

import FileChangerGUI
import tkinter

folderPath = ""
oldFileExtension = ""
newFileExtension = ""

def getFoldersButtonFunctionality():
    tkinter.Tk().withdraw()
    fn = askdirectory()
    FileChangerGUI.folderLocationInputSource.config(state=tkinter.NORMAL)
    FileChangerGUI.folderLocationInputSource.insert(tkinter.END, fn)
    FileChangerGUI.folderLocationInputSource.config(state=tkinter.DISABLED)

def changeFileExtensionsButtonFunctionality():
    folderPath = FileChangerGUI.folderLocationInputSource.get()
    oldFileExtension = FileChangerGUI.oldFileExtensionInput.get()
    FileChangerGUI.oldFileExtensionOutputArea.config(state=tkinter.NORMAL)
    FileChangerGUI.newFileExtensionOutputArea.config(state=tkinter.NORMAL)
    for file in os.listdir(folderPath):
        if file.endswith(oldFileExtension):
            print("debug") # continue implementation here.
    FileChangerGUI.oldFileExtensionOutputArea.config(state=tkinter.DISABLED)
    FileChangerGUI.newFileExtensionOutputArea.config(state=tkinter.DISABLED)

def clearUIButtonFunctionality():
    print("debug")