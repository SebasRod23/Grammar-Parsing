from Grammar import Grammar
from Node import Node
from Tree import Tree
from tkinter import *

path = "test1.txt"
grammar: Grammar
tree: Tree


# string="S"
# height=1

def Render(string, height):
    global path, grammar, tree, canvas
    grammar = ReadFile(path)
    if CheckString(string, grammar.terminal):
        # Make tree
        print("String valid")
        tree=grammar.MakeTree(string, int(height))
        tree.RenderTree(canvas)
    else:
        print("String not valid")

def CheckString(string:str, terminal):
    if len(string)==0: return False
    for i in range(len(string)):
        if string[i].isupper(): return False
        state=False
        for j in range(len(terminal)):
            if string[i]==terminal[j]: state=True
        if not state: return False
    return True

def ChooseFile(num):
    global path
    path = "test{}.txt".format(num)


def ReadFile(path):
    file = open(path, "r")
    lines = file.readlines()
    # print(lines)
    file.close()

    # Remove the enter in every line
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")

    # Not-terminal symbols alphabet
    not_Terminal = lines[0].split(",")
    # print(not_Terminal)

    # Terminal symbols alphabet
    terminal = lines[1].split(",")
    # print(terminal)

    # Starting non-terminal symbol
    start = lines[2]
    # print(start)

    # Productions
    productions = []
    for i in range(3, len(lines)):
        temp = lines[i].split("->")
        productions.append((temp[0], temp[1]))
    # print(productions)

    return Grammar(not_Terminal, terminal, Node(start, None), productions)



# grammar=ReadFile(ChooseFile())
# print("--------")
# tree=grammar.MakeTree("abbbb", 4)
# tree.PrintTree(0, tree.root, "")
# print(tree.answer)
mainWindow = Tk()
mainWindow.title("Parsing Tree")
screen_width = mainWindow.winfo_screenwidth() - 50
screen_height = mainWindow.winfo_screenheight() - 100
mainWindow.geometry("{}x{}".format(screen_width, screen_height))
mainWindow.configure(bg='red')
mainWindow.resizable(0, 0)

canvas = Canvas(mainWindow, bg="blue", height=screen_height - 50, bd=0, highlightthickness=0, relief='ridge')
canvas.pack(side=TOP, fill=X)
infoFrame = Frame(mainWindow, bg="green", height=50)
infoFrame.pack(side=BOTTOM, fill=X)

lblSelect = Label(infoFrame, text="Select an input file:", height=50)
lblSelect.pack(side=LEFT, padx=(20, 0))

bttnOne = Button(infoFrame, text="File 1", width=15, height=40, command=lambda: ChooseFile(1))
bttnOne.pack(side=LEFT, padx=(20, 0), pady=5)
bttnTwo = Button(infoFrame, text="File 2", width=15, height=40, command=lambda: ChooseFile(2))
bttnTwo.pack(side=LEFT, pady=5)
bttnThree = Button(infoFrame, text="File 3", width=15, height=40, command=lambda: ChooseFile(3))
bttnThree.pack(side=LEFT, pady=5)
bttnFour = Button(infoFrame, text="File 4", width=15, height=40, command=lambda: ChooseFile(4))
bttnFour.pack(side=LEFT, pady=5)

lblString = Label(infoFrame, text="String:", height=50)
lblString.pack(side=LEFT, padx=(40, 0))
txtString = Entry(infoFrame, width=30)
txtString.pack(side=LEFT, padx=(5, 0))

lblHeight = Label(infoFrame, text="Height:", height=50)
lblHeight.pack(side=LEFT, padx=(20, 0))
spbHeight = Spinbox(infoFrame, from_=1, to=10)
spbHeight.pack(side=LEFT, padx=(10, 0))

bttnRender = Button(infoFrame, text="Render", width=15, height=40, command=lambda: Render(txtString.get(), spbHeight.get()))
bttnRender.pack(side=RIGHT, padx=(0, 30), pady=5)

mainWindow.mainloop()
