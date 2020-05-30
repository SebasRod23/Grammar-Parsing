from Tree import Tree
from Node import Node
class Grammar():
    def __init__(self, notTerminal, terminal, start: Node, productions):
        self.not_Terminal=notTerminal
        self.terminal=terminal
        self.start=start
        self.productions=productions

    def GetLeftMostIndex(self, string):
        for i in range(len(string)):
            if string[i].isupper():
                return i
        return -1
    def CheckForNonTerminalSymbols(self, string, symbol):
        print("Symbol to Analyze {} in {}".format(symbol, string))
        for i in range(len(string)):
            if string[i]==symbol: return True
        return False

    def CheckIfPossible(self, symbol, fromIndex):
        for i in range(fromIndex, len(self.productions)):
            if self.productions[i][0] == symbol: return True
        return False

    def MakeTree(self, string)->Tree:
        tree=Tree(self.start)
        queue=[]
        queue.append(self.start)
        temp=[""]*3
        while len(queue)!=0 and string !=""+temp[0]+temp[1]+temp[2]:
            q=queue.pop(0)
            i=0
            done=False
            temp=q.label
            leftmost = temp[self.GetLeftMostIndex(temp)]
            temp = temp.split(leftmost)
            temp.insert(1, leftmost)
            while done==False and string!=temp[0]+temp[1]+temp[2] and i<len(self.productions):
                print("temp={} + {} + {}".format(temp[0],temp[1],temp[2]))
                print("Current production: {} -> {}".format(self.productions[i][0], self.productions[i][1]))
                j=i+1

                if self.CheckIfPossible(temp[1], i)==False:
                    done=True

                else:
                    print("Enter")
                    # if self.productions[i][0] == temp[1]: temp[1] = self.productions[i][1]
                    #for j in range(i+1,len(self.not_Terminal)):
                    #    if self.productions[j][0]==temp[1]: break

                    if self.CheckForNonTerminalSymbols(temp[0]+temp[1]+temp[2], self.productions[i][0]):
                        child=Node(temp[0]+self.productions[i][1]+temp[2], q)
                        q.addChild(child)
                        queue.append(child)
                        print("Queue", end=": ")
                        print(queue)
                        """temp=temp[0]+temp[1]+temp[2]
                        leftmost = temp[self.GetLeftMostIndex(temp)]
                        temp = temp.split(leftmost)
                        temp.insert(1, leftmost)"""
                i=j
                print("Done? {}".format(done))
                print()

        if string==temp[0]+temp[1]+temp[2]: print("TRUE")
        else: print("FALSE")
        return tree