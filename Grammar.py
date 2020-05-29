from Tree import Tree
from Node import Node
class Grammar():
    def __init__(self, notTerminal, terminal, start: Node, productions):
        self.not_Terminal=notTerminal
        self.terminal=terminal
        self.start=start
        self.productions=productions
        self.productionIndex=0

    def GetLeftMostIndex(self, string):
        leftmost=-1
        for i in range(len(string)):
            if string[i].isupper(): leftmost=i
        return leftmost
    def CheckForNonTerminalSymbols(self, string):
        for i in range(len(string)):
            if string[i].isupper():
                for j in range(len(self.not_Terminal)):
                    if string[i]==self.not_Terminal[j]: return True
        return False

    def CheckNextProduction(self, ntSymbol):
        for i in range(self.productionIndex,len(self.not_Terminal)):
            if self.productions[i][0]==ntSymbol:
                ntSymbol=i
                return self.productions[i][1]
        return -1

    def MakeTree(self, string)->Tree:
        tree=Tree(self.start)
        queue=[]
        queue.append(self.start)
        while len(queue)!=0:
            q=queue.pop(0)
            i=0
            found=False
            leftmost=q[self.GetLeftMostIndex(q)]
            temp=q.split(leftmost)
            temp.insert(1, leftmost)
            while found==False:
                j=i+1
                if self.GetLeftMostIndex(temp[0])==-1 or self.GetLeftMostIndex(temp[2])==-1: found=True
                else:
                    # temp[1]=self.productions[]
                    if self.CheckForNonTerminalSymbols(temp[0]+temp[1]+temp[2]):
                        queue.append(temp[0]+temp[1]+temp[2])
                        q.addChild(Node(temp[0]+temp[1]+temp[2]),q)


        return tree