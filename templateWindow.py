import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):

    selectedFiles = []  #empty list of files

    def __init__(self, master=None):
        master.title("Template")                                    #change title here
        master.geometry("300x300")                                  #change window size here
        master.resizable(width=False, height=False)                 #resizable?
        tk.Frame.__init__(self, master, relief=tk.GROOVE)
        self.menubar = tk.Menu(self)

        self.menu = tk.Menu(self.menubar, tearoff=0)
        self.addMenus(self.menu)

        self.contentFrame = tk.Frame(master, width=100, height=100)
        self.contentFrame.pack(anchor=tk.NW, fill=tk.BOTH, expand=True)

        self.addContent(self.contentFrame)

        master.config(menu=self.menubar)

    def addMenus(self, menu=None):  #add menu items here
        self.menubar.add_cascade(label="File", menu=menu)
        menu.add_command(label="Open", command=self.openFiles)
        menu.add_command(label="DEBUG|Print Open Files", command=lambda: print(self.selectedFiles))
        menu.add_command(label="Clear Selections", command=self.clearSelections)
        menu.add_separator()
        menu.add_command(label="Exit", command=self.master.quit)

    def clearSelections(self):
        self.selectedFiles.clear()

    def addContent(self, contentFrame=None):                        #add content to contentFrame here
        pass
        # self.lb = tk.Listbox(contentFrame, width=30)
        # self.lb.pack(anchor=tk.CENTER)

    def openFiles(self):                                            #change filedialog config as needed
        self.selectedFiles += filedialog.askopenfilenames(initialdir="Documents", title="Select Files", filetypes=(("Python Files","*.py"),("All Files","*.*")))
        # #updating list inside contentFrame
        # list = self.contentFrame.winfo_children()
        # if isinstance(list[0], tk.Listbox):
        #     list[0].insert(tk.END, self.selectedFiles)

root = tk.Tk()
application = Application(root)
application.pack()
root.mainloop()