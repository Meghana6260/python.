

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
        
def printBottomViewOfBinaryTree(root):
    result = []
 
    Q = [[root, 0]]
    store = dict()
    while len(Q) > 0:
        currPair = Q.pop(0)
        node = currPair[0]
        hd = currPair[1]
        store[hd] = node.data 
 
        if node.left != None:
            Q.append([node.left, hd - 1])
 
        if node.right != None:
            Q.append([node.right, hd + 1])
    allKeys = sorted(store.keys())
    for eachKey in allKeys:
        result.append(store[eachKey])
 
    # print("Top view of binary-tree is:")
    print(*result)
root=node(11)
obj2=node(7)
obj3=node(15)
obj4=node(5)
obj5=node(9)
obj6=node(13)
obj7=node(20)
obj8=node(3)
obj9=node(8)
obj10=node(10)
obj11=node(12)
obj12=node(14)
obj13=node(18)
obj14=node(25)

root.left=obj2
root.right=obj3

obj2.left=obj4
obj2.right=obj5

obj3.left=obj6
obj3.right=obj7

obj4.left=obj8
obj5.left=obj9
obj5.right=obj10
obj6.left=obj11
obj6.right=obj12
obj7.left=obj13
obj7.right=obj14

printBottomViewOfBinaryTree(root)
