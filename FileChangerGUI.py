import tkinter
import os
from shutil import which
from tkinter import scrolledtext

mainWindow = tkinter.Tk()
mainWindow.title("File Changer")
mainWindow.geometry("500x500")

folderLocationInput = tkinter.Entry(mainWindow, state=tkinter.DISABLED)
folderLocationInput.pack(side=tkinter.TOP, padx=10, pady=50)
folderLocationInput.place(x=130, y=27, width=155, height=23)

getFolderLocationButton = tkinter.Button(mainWindow, text="Get Folder")
getFolderLocationButton.pack(side=tkinter.TOP, padx=10, pady=50)
getFolderLocationButton.place(x=300, y=25)

oldFileExtensionInputLabel = tkinter.Label(mainWindow, text="Enter Old File Extension:")
oldFileExtensionInputLabel.pack(side=tkinter.TOP, padx=10, pady=50)
oldFileExtensionInputLabel.place(x=100, y=68, width=155, height=23)

oldFileExtensionInput = tkinter.Entry(mainWindow, state=tkinter.DISABLED)
oldFileExtensionInput.pack(side=tkinter.TOP, padx=10, pady=50)
oldFileExtensionInput.place(x=250, y=70)

newFileExtensionInputLabel = tkinter.Label(mainWindow, text="Enter New File Extension:")
newFileExtensionInputLabel.pack(side=tkinter.TOP, padx=10, pady=50)
newFileExtensionInputLabel.place(x=100, y=105, width=155, height=23)

newFileExtensionInput = tkinter.Entry(mainWindow, state=tkinter.DISABLED)
newFileExtensionInput.pack(side=tkinter.TOP, padx=10, pady=50)
newFileExtensionInput.place(x=250, y=107)

changeFileExtensionsButton = tkinter.Button(mainWindow, text="Change File Extensions")
changeFileExtensionsButton.pack(side=tkinter.TOP, padx=10, pady=50)
changeFileExtensionsButton.place(x=185, y=150)

oldFileExtensionOutputArea = scrolledtext.ScrolledText(mainWindow, wrap=tkinter.WORD, width=58, height=18, state=tkinter.DISABLED)
oldFileExtensionOutputArea.pack(side=tkinter.BOTTOM, padx=10, pady=50)
oldFileExtensionOutputArea.place(x=10, y=200, width=235)

newFileExtensionOutputArea = scrolledtext.ScrolledText(mainWindow, wrap=tkinter.WORD, width=58, height=18, state=tkinter.DISABLED)
newFileExtensionOutputArea.pack(side=tkinter.BOTTOM, padx=10, pady=50)
newFileExtensionOutputArea.place(x=252, y=200, width=240)

mainWindow.mainloop()