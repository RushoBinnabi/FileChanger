# Name: Rusho Binnabi
# Date: 6/11/2025
# Project: FileChanger - Launcher and Commands
# Contact Information: RushoBinnabi123@yahoo.com

from tkinter.filedialog import askdirectory
import os

import FileChangerGUI
import tkinter

# this FileChangerLauncherAndCommands file has all the code needed for the program to function.

folderPath = ""
oldFileExtension = ""
newFileExtension = ""
fileNameAndExtension = ""

# this def getFoldersButtonFunctionality() function gets the folder path of the files
# when the appropriate button is clicked.

def getFoldersButtonFunctionality():
    tkinter.Tk().withdraw()
    fn = askdirectory()
    FileChangerGUI.folderLocationInputSource.config(state=tkinter.NORMAL)
    FileChangerGUI.folderLocationInputSource.insert(tkinter.END, fn)
    FileChangerGUI.folderLocationInputSource.config(state=tkinter.DISABLED)

# this changeFileExtensionsButtonFunctionality() function changes the file extensions of the list of files
# from the folder gotten from the getFoldersButtonFunctionality() function when the appropriate button is clicked.

def changeFileExtensionsButtonFunctionality():
    folderPath = FileChangerGUI.folderLocationInputSource.get()
    oldFileExtension = FileChangerGUI.oldFileExtensionInput.get()
    newFileExtension = FileChangerGUI.newFileExtensionInput.get()
    FileChangerGUI.oldFileExtensionOutputArea.config(state=tkinter.NORMAL)
    FileChangerGUI.newFileExtensionOutputArea.config(state=tkinter.NORMAL)
    for file in os.listdir(folderPath):
        fileNameAndExtension = os.path.splitext(file)
        if fileNameAndExtension[1] == oldFileExtension.replace(oldFileExtension, "." + oldFileExtension):
            os.rename(fileNameAndExtension[0] + oldFileExtension.replace(oldFileExtension, "." + oldFileExtension), fileNameAndExtension[0] + newFileExtension.replace(newFileExtension, "." + newFileExtension))
        FileChangerGUI.oldFileExtensionOutputArea.insert(tkinter.END, fileNameAndExtension[0] + oldFileExtension.replace(oldFileExtension, "." + oldFileExtension) + "\n")
        FileChangerGUI.newFileExtensionOutputArea.insert(tkinter.END, fileNameAndExtension[0] + newFileExtension.replace(newFileExtension, "." + newFileExtension) + "\n")
    FileChangerGUI.oldFileExtensionOutputArea.config(state=tkinter.DISABLED)
    FileChangerGUI.newFileExtensionOutputArea.config(state=tkinter.DISABLED)

# this clearUIButtonFunctionality() function clears the UI when the appropriate button is clicked.

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