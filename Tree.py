from Node import Node
class Tree():
    def __init__(self, root: Node):
        self.root = root
        self.height = 1

    def PrintTree(self, level, node: Node, indent):
        print(indent+"|"+"_" * 3 + node.label)
        for i in range(len(node.childs)-1):
            self.PrintTree(level + 1, node.childs[i], indent+"\t|")
        if len(node.childs)>0:
            index=len(node.childs)-1
            self.PrintTree(level+1, node.childs[index], indent+"\t")
            print(indent)

        #print("\t|"*(level))

