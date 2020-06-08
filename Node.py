from tkinter import *


class Node():
    """Node's constructor
    :param string: the label of the node
    :param parent: the node's parent, if it is the root then it is null
    """
    def __init__(self, string, parent):
        self.label = string
        self.parent = parent
        self.childs = []
        self.color = "#730C0C"
        self.space = ((0, 0), (0, 0))
        self.center = (0, 0)

    """Adds a given node as a child of this node
    :param child: node to be added to this node's childs
    """
    def addChild(self, child):
        self.childs.append(child)
    """Changes the color of the path to this node for a given color
    :param color: the color to be changed
    """
    def changeColor(self, color):
        temp: Node
        temp = self
        while temp != None:
            temp.color = color
            temp = temp.parent

    """Draws this node in the canvas
    :param radius: the radius of the circle that will be drawn in the canvas
    :param canvas: the canvas where this node will be drawn
    :type canvas: tkinter.Canvas
    """
    def PlaceNode(self, radius, canvas: Canvas):
        center = (self.space[1][0] - self.space[0][0], self.space[1][1] - self.space[0][1])
        center = (self.space[0][0] + center[0] / 2, self.space[0][1] + center[1] / 2)
        self.center = center
        circle = canvas.create_oval(center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius,
                                    fill=self.color)
        font="verdana"
        mult=0.5
        text = canvas.create_text(center[0], center[1], text=self.label, fill="white", font=(font, int(mult * radius)))
        canvas.tag_raise(text)
        canvas.tag_lower(circle)

    """Draws a line in the canvas between this node and its parent if the latter is not null
        :param canvas: the canvas where this node will be drawn
        :type canvas: tkinter.Canvas
        """
    def PlaceLine(self, canvas: Canvas):
        if self.parent != None:
            line = canvas.create_line(self.center[0], self.center[1], self.parent.center[0], self.parent.center[1],
                                      fill="white")
            canvas.tag_lower(line)

    def __str__(self):
        return self.label

    def __repr__(self):
        return self.label
