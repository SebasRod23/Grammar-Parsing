from Tree import Tree
from Node import Node


class Grammar():
    """Grammar constructor
    :param notTerminal: array of str of the non-terminal symbols
    :param terminal: array of str of the terminal symbols
    :param start: starting node
    :type start: Node
    :param productions: array of pairs that represent the productions of the grammar
    """

    def __init__(self, notTerminal, terminal, start: Node, productions):
        self.not_Terminal = notTerminal
        self.terminal = terminal
        self.start = start
        self.productions = productions

    """Check the given string and return the index of the leftmost non-terminal symbol
    :param string: the str to be analyzed
    :returns: leftmost not-terminal symbol's index
    """

    def GetLeftMostIndex(self, string):
        for i in range(len(string)):
            if string[i].isupper():
                return i
        return -1

    """Check the string and return True if you find the given non-terminal symbol in the string, otherwise return False
    :param string: the str to be analyzed
    :param symbol: the non-terminal symbol to find
    :returns: True if found symbol in string, otherwise returns False
    """

    def CheckForNonTerminalSymbols(self, string, symbol):
        for i in range(len(string)):
            if string[i] == symbol: return True
        return False

    """Check the string and return True if you find the given non-terminal symbol in the productions of the grammar not yet used, otherwise returns False
        :param symbol: the non-terminal symbol to find
        :param fromIndex: the index from where to start
        :returns: True if found symbol in productions from the starting index, otherwise returns False
        """

    def CheckIfPossible(self, symbol, fromIndex):
        for i in range(fromIndex, len(self.productions)):
            if self.productions[i][0] == symbol: return True
        return False

    # Make logical and print the tree
    """Returns the parsing tree of the grammar given a string and a max depth and if found it prints the tree in the console and changes the color of the path to the string in the GUI
    :param string: the str to be searched in the tree
    :param maxDepth: the max depth in which the given string will be searched
    :returns: the parsing tree of the grammar, either with the string having been found or not
    :rtype: Tree
    """
    def MakeTree(self, string, maxDepth) -> Tree:
        tree = Tree(self.start)
        queue = []
        queue.append(self.start)
        temp = [""] * 3
        child = Node("", None)
        while len(queue) != 0 and maxDepth >= tree.CheckDepth():
            q = queue.pop(0)
            i = 0
            done = False
            leftmost = self.GetLeftMostIndex(q.label)
            temp = [""] * 3
            temp[0] = q.label[0:leftmost]
            temp[1] = q.label[leftmost]
            temp[2] = q.label[leftmost + 1:]
            while done == False and i < len(self.productions) and maxDepth >= tree.CheckDepth():
                j = i + 1

                if not self.CheckIfPossible(temp[1], i):
                    done = True

                else:
                    if self.CheckForNonTerminalSymbols(temp[0] + temp[1] + temp[2], self.productions[i][0]):
                        child = Node(temp[0] + self.productions[i][1] + temp[2], q)
                        if child.label == string:
                            tree.answer = child
                            child.changeColor("#0C4D07")
                        q.addChild(child)
                        queue.append(child)
                i = j
        temp = queue.pop(len(queue) - 1)
        pTemp = temp.parent
        pTemp.childs.remove(temp)
        tree.PrintTree(0, tree.root, "")
        if tree.answer != None:
            print("The string was found!")
        else:
            print("The string was not found")
        print("-----------------------------------------")

        return tree
