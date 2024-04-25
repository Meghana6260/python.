class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,ele):
    if root==None:
        newblock=node(ele)
        return newblock

    if root.data<ele:
        root.right=insert(root.right,ele)
    else:
        root.left=insert(root.left,ele)
    return root                

def inorder(root):
    if root==None:
        return
    inorder(root.left)    
    print(root.data,end=" ")
    inorder(root.right)    
root=None
n=int(input())
nums=list(map(int,input().split()))
for ele in nums:
    root=insert(root,ele)
inorder(root)
