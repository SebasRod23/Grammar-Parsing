from Grammar import Grammar
from Node import Node
from Tree import Tree
from tkinter import *
from tkinter import messagebox

# Default path and type assignation
path = "test1.txt"
grammar: Grammar
tree: Tree


def Render(string, height):
    global path, grammar, tree, canvas, mainWindow
    grammar = ReadFile(path)
    if CheckString(string, grammar.terminal):
        print("-----------------------------------------")
        print("Creating parsing-tree for: " + string+", with height: {}".format(height))
        print("-----------------------------------------")
        # Make tree
        tree = grammar.MakeTree(string, int(height))
        # Render Tree
        tree.RenderTree(canvas)
    else:
        message = 'The input: "{}" is not accepted, use only terminal symbols of the {}'.format(string,
                                                                                                path.upper()) + "'s terminal alphabet: {}".format(
            grammar.terminal)
        messagebox.showinfo(title="Invalid input", message=message)


def CheckString(string: str, terminal):
    if len(string) == 0: return False
    for i in range(len(string)):
        if string[i].isupper(): return False
        state = False
        for j in range(len(terminal)):
            if string[i] == terminal[j]: state = True
        if not state: return False
    return True


def ChooseFile(num):
    global path, bttnOne, bttnTwo, bttnThree, bttnFour
    colorSelected = "#625E5E"
    path = "test{}.txt".format(num)
    bttnOne.config(bg="white")
    bttnTwo.config(bg="white")
    bttnThree.config(bg="white")
    bttnFour.config(bg="white")
    if num == 1:
        bttnOne.config(bg=colorSelected)
    elif num == 2:
        bttnTwo.config(bg=colorSelected)
    elif num == 3:
        bttnThree.config(bg=colorSelected)
    elif num == 4:
        bttnFour.config(bg=colorSelected)


def ReadFile(path):
    print("Reading " + path)
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

# Window script

# Color for buttons when selected
colorBottom = "#282626"

# Create the Main Window for the app
mainWindow = Tk()
mainWindow.title("Parsing Tree")
screen_width = mainWindow.winfo_screenwidth() - 50
screen_height = mainWindow.winfo_screenheight() - 100
mainWindow.geometry("{}x{}".format(screen_width, screen_height))
mainWindow.resizable(0, 0)
mainWindow.iconbitmap(default="icon.ico")

# Create the Canvas where the tree will be rendered
canvas = Canvas(mainWindow, bg="#000000", height=screen_height - 50, bd=0, highlightthickness=0, relief='ridge')
canvas.pack(side=TOP, fill=X)

# Create the bottom frame for the buttons and inputs
infoFrame = Frame(mainWindow, bg=colorBottom, height=50)
infoFrame.pack(side=BOTTOM, fill=X)

# File selection label with instructions and buttons with their corresponding files
lblSelect = Label(infoFrame, text="Select an input file:", height=50, bg=colorBottom, fg="white")
lblSelect.pack(side=LEFT, padx=(20, 0))
bttnOne = Button(infoFrame, text="File 1", width=15, height=40, bg="#625E5E", command=lambda: ChooseFile(1))
bttnOne.pack(side=LEFT, padx=(20, 0), pady=5)
bttnTwo = Button(infoFrame, text="File 2", width=15, height=40, command=lambda: ChooseFile(2))
bttnTwo.pack(side=LEFT, pady=5)
bttnThree = Button(infoFrame, text="File 3", width=15, height=40, command=lambda: ChooseFile(3))
bttnThree.pack(side=LEFT, pady=5)
bttnFour = Button(infoFrame, text="File 4", width=15, height=40, command=lambda: ChooseFile(4))
bttnFour.pack(side=LEFT, pady=5)

# Entry for string input
lblString = Label(infoFrame, text="String:", height=50, bg=colorBottom, fg="white")
lblString.pack(side=LEFT, padx=(40, 0))
txtString = Entry(infoFrame, width=30)
txtString.pack(side=LEFT, padx=(5, 0))

# Spinbox for height of the tree
lblHeight = Label(infoFrame, text="Height:", height=50, bg=colorBottom, fg="white")
lblHeight.pack(side=LEFT, padx=(20, 0))
spbHeight = Spinbox(infoFrame, from_=1, to=10)
spbHeight.pack(side=LEFT, padx=(10, 0))

# Button to Render the tree
bttnRender = Button(infoFrame, text="Render", width=15, height=40,
                    command=lambda: Render(txtString.get(), spbHeight.get()))
bttnRender.pack(side=RIGHT, padx=(0, 30), pady=5)

mainWindow.mainloop()
