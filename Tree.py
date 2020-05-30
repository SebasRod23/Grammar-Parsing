from Node import Node
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

    def PrintTree(self, level, node: Node, indent):
        print(indent+"|"+"_" * 3 + node.label)
        for i in range(len(node.childs)-1):
            self.PrintTree(level + 1, node.childs[i], indent+"\t|")
        if len(node.childs)>0:
            index=len(node.childs)-1
            self.PrintTree(level+1, node.childs[index], indent+"\t")
            print(indent)

        #print("\t|"*(level))

