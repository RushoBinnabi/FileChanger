from tkinter.filedialog import askdirectory
import os

import FileChangerGUI
import tkinter

folderPath = ""
oldFileExtension = ""
newFileExtension = ""
fileNameAndExtension = ""

def getFoldersButtonFunctionality():
    tkinter.Tk().withdraw()
    fn = askdirectory()
    FileChangerGUI.folderLocationInputSource.config(state=tkinter.NORMAL)
    FileChangerGUI.folderLocationInputSource.insert(tkinter.END, fn)
    FileChangerGUI.folderLocationInputSource.config(state=tkinter.DISABLED)

def changeFileExtensionsButtonFunctionality():
    folderPath = FileChangerGUI.folderLocationInputSource.get()
    oldFileExtension = FileChangerGUI.oldFileExtensionInput.get()
    newFileExtension = FileChangerGUI.newFileExtensionInput.get()
    FileChangerGUI.oldFileExtensionOutputArea.config(state=tkinter.NORMAL)
    FileChangerGUI.newFileExtensionOutputArea.config(state=tkinter.NORMAL)
    for file in os.listdir(folderPath):
        fileNameAndExtension = os.path.splitext(file)
        if fileNameAndExtension[1] == oldFileExtension:
            os.rename(fileNameAndExtension[0] + oldFileExtension, fileNameAndExtension[0] + newFileExtension)
        FileChangerGUI.oldFileExtensionOutputArea.insert(tkinter.END, fileNameAndExtension[0] + oldFileExtension + "\n")
        FileChangerGUI.newFileExtensionOutputArea.insert(tkinter.END, fileNameAndExtension[0] + newFileExtension + "\n")
    FileChangerGUI.oldFileExtensionOutputArea.config(state=tkinter.DISABLED)
    FileChangerGUI.newFileExtensionOutputArea.config(state=tkinter.DISABLED)

def clearUIButtonFunctionality():
    FileChangerGUI.oldFileExtensionOutputArea.config(state=tkinter.NORMAL)
    FileChangerGUI.newFileExtensionOutputArea.config(state=tkinter.NORMAL)
    FileChangerGUI.folderLocationInputSource.config(state=tkinter.NORMAL)
    FileChangerGUI.oldFileExtensionInput.delete(0, tkinter.END)
    FileChangerGUI.newFileExtensionInput.delete(0, tkinter.END)
    FileChangerGUI.oldFileExtensionOutputArea.delete(1.0, tkinter.END)
    FileChangerGUI.newFileExtensionOutputArea.delete(1.0, tkinter.END)
    FileChangerGUI.folderLocationInputSource.delete(0, tkinter.END)
    FileChangerGUI.oldFileExtensionOutputArea.config(state=tkinter.DISABLED)
    FileChangerGUI.newFileExtensionOutputArea.config(state=tkinter.DISABLED)
    FileChangerGUI.folderLocationInputSource.config(state=tkinter.DISABLED)