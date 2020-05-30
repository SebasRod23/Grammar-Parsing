class Node():
    def __init__(self, string, parent):
        self.label=string
        self.parent=parent
        self.childs=[]

    def addChild(self, child):
        self.childs.append(child)

    def __str__(self):
        return self.label
    def __repr__(self):
        return self.label