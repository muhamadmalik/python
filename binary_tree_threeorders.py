class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item



def inorder(root):
    if root:
        inorder(root.left)
        print(f"| {root.val} |")
        inorder(root.right)
        
def preorder(root):
    if root:
        print(f"| {root.val} |")
        preorder(root.left)
        preorder(root.right)
        pass
    pass
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(f"| {root.val} |")


root = Node(1)
root.left = Node(12)
root.right = Node(9)
root.left.left = Node(5)
root.left.right = Node(6)
print("InOrder")
inorder(root)
print('PreOrder')
preorder(root)
print("PostOrder")
postorder(root)