class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructBSTFromPreorder(preorder):
    if not preorder:
        return None

    lower=float('-inf')
    upper=float('inf')
    if not preorder or preorder[0] < lower or preorder[0] > upper:
        return None
    root_val = preorder.pop(0)
    root = TreeNode(root_val)

    return root

def getRootValue(root):
    return root.val if root else None

# Example usage:
preorder1 = input("")
preorder = [int(digit) for digit in preorder1.strip('[],\r,\n,[,], ').split(', ')]
root = constructBSTFromPreorder(preorder)

# Get the root value
root_value = getRootValue(root)
print(root_value)