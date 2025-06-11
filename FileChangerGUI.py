# Name: Rusho Binnabi
# Date: 6/11/2025
# Project: FileChanger - GUI
# Contact Information: RushoBinnabi123@yahoo.com

import tkinter
from tkinter import scrolledtext
import FIleChangerLauncherAndCommands

# this FileChangerGUI file has all the code needed for the GUI setup.

mainWindow = tkinter.Tk()
mainWindow.title("File Changer")
mainWindow.geometry("500x500")

folderLocationInputSource = tkinter.Entry(mainWindow, state=tkinter.DISABLED)
folderLocationInputSource.pack(side=tkinter.TOP, padx=10, pady=50)
folderLocationInputSource.place(x=130, y=27, width=155, height=23)

getFolderLocationButton = tkinter.Button(mainWindow, text="Get Folder", command=FIleChangerLauncherAndCommands.getFoldersButtonFunctionality)
getFolderLocationButton.pack(side=tkinter.TOP, padx=10, pady=50)
getFolderLocationButton.place(x=300, y=25)

oldFileExtensionInputLabel = tkinter.Label(mainWindow, text="Enter Old File Extension:")
oldFileExtensionInputLabel.pack(side=tkinter.TOP, padx=10, pady=50)
oldFileExtensionInputLabel.place(x=100, y=68, width=155, height=23)

oldFileExtensionInput = tkinter.Entry(mainWindow)
oldFileExtensionInput.pack(side=tkinter.TOP, padx=10, pady=50)
oldFileExtensionInput.place(x=250, y=70)

newFileExtensionInputLabel = tkinter.Label(mainWindow, text="Enter New File Extension:")
newFileExtensionInputLabel.pack(side=tkinter.TOP, padx=10, pady=50)
newFileExtensionInputLabel.place(x=100, y=105, width=155, height=23)

newFileExtensionInput = tkinter.Entry(mainWindow)
newFileExtensionInput.pack(side=tkinter.TOP, padx=10, pady=50)
newFileExtensionInput.place(x=250, y=107)

changeFileExtensionsButton = tkinter.Button(mainWindow, text="Change File Extensions", command=FIleChangerLauncherAndCommands.changeFileExtensionsButtonFunctionality)
changeFileExtensionsButton.pack(side=tkinter.TOP, padx=10, pady=50)
changeFileExtensionsButton.place(x=135, y=150)

clearUIButton = tkinter.Button(mainWindow, text="Clear", command=FIleChangerLauncherAndCommands.clearUIButtonFunctionality)
clearUIButton.pack(side=tkinter.TOP, padx=10, pady=50)
clearUIButton.place(x=280, y=150)

oldFileExtensionOutputArea = scrolledtext.ScrolledText(mainWindow, wrap=tkinter.WORD, width=58, height=18, state=tkinter.DISABLED)
oldFileExtensionOutputArea.pack(side=tkinter.BOTTOM, padx=10, pady=50)
oldFileExtensionOutputArea.place(x=10, y=200, width=235)

newFileExtensionOutputArea = scrolledtext.ScrolledText(mainWindow, wrap=tkinter.WORD, width=58, height=18, state=tkinter.DISABLED)
newFileExtensionOutputArea.pack(side=tkinter.BOTTOM, padx=10, pady=50)
newFileExtensionOutputArea.place(x=252, y=200, width=240)

mainWindow.mainloop()