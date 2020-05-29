class Node():
    def __init__(self, string, parent):
        self.label=string
        self.parent=parent
        self.childs=[]

    def addChild(self, child):
        self.childs.append(child)