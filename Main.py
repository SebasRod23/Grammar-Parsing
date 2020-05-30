from Grammar import Grammar
from Node import Node
from Tree import Tree

def ChooseFile():
    return "test" + input("Select a test file: ") + ".txt"


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
    print(not_Terminal)

    # Terminal symbols alphabet
    terminal = lines[1].split(",")
    print(terminal)

    # Starting non-terminal symbol
    start = lines[2]
    print(start)

    # Productions
    productions=[]
    for i in range(3, len(lines)):
        temp = lines[i].split("->")
        productions.append((temp[0], temp[1]))
    print(productions)

    return Grammar(not_Terminal,terminal,Node(start, None),productions)

grammar=ReadFile(ChooseFile())
print("--------")
tree=grammar.MakeTree("abbbb", 6)
tree.PrintTree(0, tree.root, "")
print(tree.answer)

