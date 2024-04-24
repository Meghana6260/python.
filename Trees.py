class TreeNOde:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=TreeNOde(18)
obj2=TreeNOde(15)
obj3=TreeNOde(20)
obj4=TreeNOde(25)
obj5=TreeNOde(30)
obj6=TreeNOde(45)
obj7=TreeNOde(80)

# Establishing links
root.left=obj2
root.right=obj3

obj2.left=obj4
obj2.right=obj5

obj3.left=obj6
obj3.right=obj7

## PREORDER ##

def printPreorder(root):
    if root==None:
        return
    print(root.data,end=" ")
    printPreorder(root.left)
    printPreorder(root.right)
printPreorder(root)    
print()

#INORDER#

def printInorder(root):
    if root==None:
        return
    printInorder(root.left)
    print(root.data ,end=" ")
    printInorder(root.right)

printInorder(root)    
print()

#POSTORDER#

def postorder(root):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")            
postorder(root)
print()
