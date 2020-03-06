import sys
import tkinter as tk
from tkinter import filedialog
import Modules.Pages as Pages

WIDTH = 400
HEIGHT = 400

class Application(tk.Frame):

    selectedFiles = []

    def __init__(self, master=None):
        master.title("Template")                                  #change title here
        master.geometry("{}x{}".format(WIDTH, HEIGHT))            #change window size here
        master.resizable(width=False, height=False)               #resizable?
        tk.Frame.__init__(self, master, relief=tk.GROOVE)
        self.menubar = tk.Menu(self)

        self.contentFrame = tk.Frame(master, width=100, height=100)
        self.contentFrame.pack(anchor=tk.NW, fill=tk.BOTH, expand=True)

        self.pages = []         # initialize pages list

        self.addContent(self.contentFrame)

        self.menus = []         # initialize menus list

        self.addMenus(self.menus)

        for page in self.pages:     # place all pages
            page.place(in_=self.contentFrame, x=0, y=0, relwidth=1, relheight=1)

        self.pages[0].show()

        master.config(menu=self.menubar)

        self.bind_all("<Control-Key-0>", self.pages[0].show)    # main menu
        self.bind_all("<Control-Key-1>", self.pages[1].show)    # Page 2

    def addMenus(self, menus=None):  #add menu items here

        self.menus.append(tk.Menu(self.menubar, tearoff=0))

        self.menubar.add_cascade(label="File", menu=menus[0])
        menus[0].add_command(label="Open", command=self.openFiles)
        menus[0].add_command(label="DEBUG|Print Open Files", command=lambda: print(self.selectedFiles))
        menus[0].add_command(label="Clear Selections", command=self.clearSelections)
        menus[0].add_separator()
        menus[0].add_command(label="Exit", command=self.master.quit)

        menus.append(tk.Menu(self.menubar, tearoff=0))  # create dropdown menu View

        self.menubar.add_cascade(label="Pages", underline=0, menu=menus[1])
        menus[1].add_command(label="Main Menu", command=self.pages[0].lift, accelerator="Control+0")
        menus[1].add_command(label="Page 1", command=self.pages[1].lift, accelerator="Control+1")

    def clearSelections(self):
        self.selectedFiles.clear()

    def addContent(self, contentFrame=None):                        #add content to contentFrame here
        self.pages.append(Pages.Menu(WIDTH))
        self.pages.append(Pages.Page2(WIDTH))
        # self.lb = tk.Listbox(contentFrame, width=30)
        # self.lb.pack(anchor=tk.CENTER)

    def openFiles(self):                                            #change filedialog config as needed
        self.selectedFiles += filedialog.askopenfilenames(initialdir="Documents", title="Select Files", filetypes=(("Python Files","*.py"),("All Files","*.*")))
        # #updating list inside contentFrame
        # list = self.contentFrame.winfo_children()
        # if isinstance(list[0], tk.Listbox):
        #     list[0].insert(tk.END, self.selectedFiles)

def handleArgs():
    pass

if __name__ == "__main__":
    handleArgs()
    root = tk.Tk()
    application = Application(root)
    application.pack()
    root.mainloop()