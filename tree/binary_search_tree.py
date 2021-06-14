from typing import no_type_check_decorator


class BSTNode:
    def __init__(self, value):
        self.data = value
        self.leftChild = None
        self.rightChild = None

    
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue < rootNode.data:
        if rootNode.leftChild == None:
            newNode = BSTNode(nodeValue)
            rootNode.leftChild = newNode
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild == None: 
            newNode = BSTNode(nodeValue)
            rootNode.rightChild = newNode
        else:
            insertNode(rootNode.rightChild, nodeValue)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)


sampleBST = BSTNode(None)
insertNode(sampleBST, 70)
insertNode(sampleBST, 50)
insertNode(sampleBST, 80)
insertNode(sampleBST, 90)
insertNode(sampleBST, 40)
insertNode(sampleBST, 10)
insertNode(sampleBST, 20)
insertNode(sampleBST, 30)

searchNode(sampleBST, 90)