import queue
class BinaryTreeNodes:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
# def printTree(root):
#     if root == None:
#         return
#     print(root.data, end = ":")
#     if root.left != None:
#         print('L', root.left.data, end=",")
#     if root.right != None:
#         print('R', root.right.data, end="")
#     print()
    
#     printTree(root.left)
#     printTree(root.right)

def printLevelWise(root):
    q = queue.Queue()
    
    if root == None:
        return None
    
    q.put(root)
    
    while(not(q.empty())):
        a = q.get()
        print(a.data, end=":")
        
        leftChild = a.left
        if leftChild != None:
            print("L:", end = "")
            print(leftChild.data, end = ",")
            q.put(leftChild)
        else:
            print("L:", end = "")
            print(-1, end = ",")
            
        rightChild = a.right
        if rightChild != None:
            print("R:", end = "")
            print(rightChild.data)
            q.put(rightChild)
        else:
            print("R:", end = "")
            print(-1)
    return root


def takeLevelWiseInput():
    q = queue.Queue()
    print('Enter root')
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = BinaryTreeNodes(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node =  q.get()
        
        print('Enter left child of', current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNodes(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
            
        print('Enter right child of', current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNodes(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
            
            
    return root

root = takeLevelWiseInput()
printLevelWise(root)
