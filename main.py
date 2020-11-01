from tkinter import Tk, RAISED, ANCHOR, END, StringVar, IntVar, Frame, Listbox, Label, Button, Checkbutton
import os

import resize 

root = Tk()
root.geometry('750x300')

class Application(Frame):
    defaultInput = os.path.join(os.path.dirname(os.path.realpath(__file__)), "original")
    defaultOutput = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resized")
    fileName = StringVar()
    inputFile = ''
    label3 = ''
    accept_files = ["jpg", "png"]

    def __init__(self, master=None):
        Frame.__init__(self, master, width=400, height=300)
        self.pack()
        self.List_Box()
        self.Create_Buttons()
        self.Resize_Options()

    def List_Box(self):
        label1 = Label(self, text="Select image to resize")
        label1.grid(row=0, column=0)
        self.inputFile = Listbox(self, width=50, font=("times", 13))
        self.UpdateListBox()
        self.inputFile.grid(row=1, column=0)
        self.label3 = Label(self, text='', fg='Green')
        self.label3.grid(row=2, column=0)

    def UpdateListBox(self):
        self.inputFile.delete(0,END)
        fileList = os.listdir(self.defaultInput)
        for i in range(len(fileList)):
            if (fileList[i][-3:] in self.accept_files):
                self.inputFile.insert(END, fileList[i])

    def Create_Buttons(self):
        label2 = Label(self, text="Select resize options")
        label2.grid(row=0, column=1)

        convert_Btn = Button(self, text="Resize image", command=self.Resize_File)
        convert_Btn.grid(row=2, column=1)
        exit_Btn = Button(self, text="Exit", command=self.Quit)
        exit_Btn.grid(row=4, column=1)

    def Resize_Options(self):
        check1 = StringVar()
        check2 = StringVar()
        check3 = StringVar()
        check1.set("0")
        check2.set("0")
        check3.set("0")
        self.options = [check1, check2, check3]
        cBtn1 = Checkbutton(self, text="800 x 600", variable=check1, onvalue = "800x600", offvalue = "0")
        cBtn2 = Checkbutton(self, text="1024 x 600", variable=check2, onvalue = "1024x600", offvalue = "0")
        cBtn3 = Checkbutton(self, text="40 x 40", variable=check3, onvalue = "40x40", offvalue = "0")
        cBtn1.grid(row=1, column=1)
        cBtn2.grid(row=1, column=2)
        cBtn3.grid(row=1, column=3)

    def Resize_File(self):
        doThings = False
        if(len(self.inputFile.get(ANCHOR)) < 1):
            self.label3['text'] = "Select a file"
            self.label3['fg'] = 'Red'
        elif(len(self.inputFile.get(ANCHOR)) > 1):
            self.label3['text'] = " "
            self.label3['fg'] = 'Green'
            doThings = True
        try:
            if(doThings == True):
                fileName = self.inputFile.get(ANCHOR)
                fileSplit = fileName.split(".")
                for opt in self.options:
                    dimensions = opt.get().split("x")
                    if dimensions[0] == '0':
                        continue
                    else:
                        filePath = os.path.join(self.defaultInput, fileName)
                        newPath = os.path.join(self.defaultOutput, self.Format_Name(fileSplit, dimensions))
                        scale = (int(dimensions[0]), int(dimensions[1]))
                        new_img = resize.resize(filePath, scale)
                        new_img.save(newPath)
                    self.label3['text'] = 'Done'
                    self.UpdateListBox()
        except AttributeError:
            self.label3['text'] = "Select resize options"
            self.label3['fg'] = 'Red'

    def Format_Name(self, fileSplit, dimensions):
        return fileSplit[0] + "_" + dimensions[0] + "x" + dimensions[1] + "." + fileSplit[1]

    def Quit(self):
        root.destroy()

appUi = Application(master=root)
appUi.mainloop()
