class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, end = ":")
    if root.left != None:
        print('L',root.left.data, end=',')
    if root.right != None:
        print('R',root.right.data, end="")
    print()
    
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)
    
def isBST2(root):
    if root == None:
        return 100000, -100000, True
    
    leftMin, leftMax, isLeftBST = isBST2(root.left)
    rightMin, rightMax, isRightBST = isBST2(root.right)
    
    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)
    
    isTreeBST = True
    if root.data <= leftMax or root.data > rightMin:
        isTreeBST = False
    if not(isLeftBST) or not(isRightBST):
        isTreeBST = False
        
    return minimum, maximum, isTreeBST     

root = treeInput()
printTreeDetailed(root) 
print(isBST2(root))