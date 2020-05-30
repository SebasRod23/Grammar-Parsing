from tkinter import *
class Node():
    def __init__(self, string, parent):
        self.label=string
        self.parent=parent
        self.childs=[]
        self.color="red"
        self.space=((0,0),(0,0))
        self.center=(0,0)

    def addChild(self, child):
        self.childs.append(child)
    def changeColor(self, color):
        temp:Node
        temp=self
        while temp!=None:
            temp.color = color
            temp = temp.parent

    def PlaceNode(self, radius, canvas: Canvas):
        radius=radius/2
        # circle=canvas.create_oval(25,25,75,75, fill="black")
        # canvas.create_text(50,50,text="Circle", fill="white")
        center=(self.space[1][0]-self.space[0][0], self.space[1][1]-self.space[0][1])
        center=(self.space[0][0]+center[0]/2, self.space[0][1]+center[1]/2)
        self.center=center
        #print("{}.center={}".format(self.label, center))
        canvas.create_oval(center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius, fill=self.color)
        canvas.create_text(center[0],center[1], text=self.label)

    def PlaceLine(self, canvas:Canvas):
        if self.parent!=None:
            line=canvas.create_line(self.center[0], self.center[1], self.parent.center[0], self.parent.center[1])
            canvas.tag_lower(line)

    def __str__(self):
        return self.label
    def __repr__(self):
        return self.label