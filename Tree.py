from Node import Node
from tkinter import *
class Tree():
    def __init__(self, root: Node):
        self.root = root
        self.answer=None

    def CheckDepth(self):
        return self.CheckMaxDepth(self.root, 1)

    def CheckMaxDepth(self, node, depth):
        if len(node.childs)==0: return depth
        maxDepth=1
        for child in node.childs:
            maxDepth=max(maxDepth, self.CheckMaxDepth(child, depth+1))
        return maxDepth

    def CheckMinSpace(self, node, minSpace):
        if len(node.childs)==0: return minSpace
        space=node.space[1][0]-node.space[0][0]
        for child in node.childs:
            space=max(space, self.CheckMaxDepth(child, minSpace+1))
        return space

    def PrintTree(self, level, node: Node, indent):
        if self.answer==node: print(indent+"|"+"_" * 3 + node.label+"---> FOUND")
        else: print(indent+"|"+"_" * 3 + node.label)
        for i in range(len(node.childs)-1):
            self.PrintTree(level + 1, node.childs[i], indent+"\t|")
        if len(node.childs)>0:
            index=len(node.childs)-1
            self.PrintTree(level+1, node.childs[index], indent+"\t")
            print(indent)

    def RenderTree(self, canvas: Canvas):
        canvas.delete("all")
        # print("Canvas width: {}, height: {}".format(canvas.winfo_width(), canvas.winfo_height()))
        # Assign space to all tree leafs
        yOffset=canvas.winfo_height()/self.CheckDepth()
        xOffset=canvas.winfo_width()
        self.root.space=((0,0),(xOffset,yOffset))
        if len(self.root.childs)>0:
            xOffset=xOffset/len(self.root.childs)
            for i in range(len(self.root.childs)):
                self.RenderLeafs(self.root.childs[i], xOffset*i, xOffset*(i+1), yOffset,yOffset*2)

        # Calculate min space
        space=self.CheckMinSpace(self.root, self.root.space[1][0]-self.root.space[0][0])
        space=min(space, self.root.space[1][1]-self.root.space[0][1])
        radius=space/2
        radius=radius-5

        # Place all nodes
        self.PlaceLeaf(self.root, radius, canvas, self.CheckDepth())



    def PlaceLeaf(self, node, radius, canvas, height):
        node.PlaceNode(radius, canvas, height)
        node.PlaceLine(canvas)
        if len(node.childs)>0:
            for child in node.childs:
                self.PlaceLeaf(child, radius, canvas, height)

    def RenderLeafs(self, node: Node, xo, xf, yo, yf):
        # print("{}: xo={}, xf={}, yo={}, yf={}".format(node.label, xo, xf, yo, yf))
        node.space=((xo,yo),(xf,yf))
        if len(node.childs)>0:
            offX=xf-xo
            offY=yf-yo
            offX=offX/len(node.childs)
            for i in range(len(node.childs)):
                self.RenderLeafs(node.childs[i], xo+offX*i, xo+offX*(i+1), yf, yf+offY)


