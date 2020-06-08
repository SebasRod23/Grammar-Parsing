from Node import Node
from tkinter import *


class Tree():

    """Tree's constructor
    :param root: the node that will act as the root of the tree
    :type root: Node
    """

    def __init__(self, root: Node):
        self.root = root
        self.answer = None

    """Checks the depth of the tree starting in the root
    :returns: the max depth of the tree
    """

    def CheckDepth(self):
        return self.CheckMaxDepth(self.root, 1)

    """Check for the maximum depth of a tree from a given node recursively
    :param node: the node from which the search will start
    :param depth: the depth 
    :returns: the max depth found from the given node
    """

    def CheckMaxDepth(self, node, depth):
        if len(node.childs) == 0: return depth
        maxDepth = 1
        for child in node.childs:
            maxDepth = max(maxDepth, self.CheckMaxDepth(child, depth + 1))
        return maxDepth

    """Checks for the minimum x-space in the canvas recursively
    :param node: the node being analyzed at the moment
    :returns: minimum space in x
    """
    def CheckMinSpace(self, node):
        space = node.space[1][0] - node.space[0][0]
        for child in node.childs:
            space = min(space, self.CheckMinSpace(child))
        return space

    # Print tree in the console
    """Prints the tree in the console
    :param level: the level of the given node inside the tree
    :param node: the node being printed
    :type node: Node
    :param indent: the indent in the printed line of the given node
    """
    def PrintTree(self, level, node: Node, indent):
        if self.answer == node:
            print(indent + "|" + "_" * 3 + node.label + "---> FOUND")
        else:
            print(indent + "|" + "_" * 3 + node.label)
        for i in range(len(node.childs) - 1):
            self.PrintTree(level + 1, node.childs[i], indent + "\t|")
        if len(node.childs) > 0:
            index = len(node.childs) - 1
            self.PrintTree(level + 1, node.childs[index], indent + "\t")
            print(indent)

    """Renders the tree in the canvas
    :param canvas: the canvas where the tree will be render
    :type canvas: tkinter.Canvas
    """
    def RenderTree(self, canvas: Canvas):
        canvas.delete("all")
        # Assign space to all tree leafs
        yOffset = canvas.winfo_height() / self.CheckDepth()
        xOffset = canvas.winfo_width()
        self.root.space = ((0, 0), (xOffset, yOffset))
        if len(self.root.childs) > 0:
            xOffset = xOffset / len(self.root.childs)
            for i in range(len(self.root.childs)):
                self.RenderLeafs(self.root.childs[i], xOffset * i, xOffset * (i + 1), yOffset, yOffset * 2)

        # Calculate minimum space
        space = self.CheckMinSpace(self.root)
        space = min(space, self.root.space[1][1] - self.root.space[0][1])
        radius = space / 2
        radius = radius - 5

        # Place all nodes
        self.PlaceLeaf(self.root, radius, canvas)

    """Places the tree's leafs in their corresponding location
    :param node: the node to  be placed
    :param radius: the node's circle radius
    :param canvas: the canvas where the node will be placed
    """
    def PlaceLeaf(self, node, radius, canvas):
        node.PlaceNode(radius, canvas)
        node.PlaceLine(canvas)
        if len(node.childs) > 0:
            for child in node.childs:
                self.PlaceLeaf(child, radius, canvas)

    # Place the nodes in the right place of the window
    """Renders the tree's leaf's space for their placement in the canvas recursively
    :param node: the node to be render
    :type node: Node
    :param xo: the initial x coordinate for the node
    :param xf: the final x coordinate for the node
    :param yo: the initial y coordinate for the node
    :param yf: the final y coordinate for the node
    """
    def RenderLeafs(self, node: Node, xo, xf, yo, yf):
        node.space = ((xo, yo), (xf, yf))
        if len(node.childs) > 0:
            offX = xf - xo
            offY = yf - yo
            offX = offX / len(node.childs)
            for i in range(len(node.childs)):
                self.RenderLeafs(node.childs[i], xo + offX * i, xo + offX * (i + 1), yf, yf + offY)
