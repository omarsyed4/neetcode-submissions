# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []

        def preorder(hRoot) -> List:
            # Base case: if the root is null. 
            if not hRoot:
                arr.append('#')
                return

            # Add the current value. 
            arr.append(str(hRoot.val))

            # Add the left and right subtrees in that order. 
            preorder(hRoot.left)
            preorder(hRoot.right)

        
        preorder(root)

        res = ",".join(arr)

        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        arr = data.split(",")

        i = 0

        def reconstruct() -> Optional[TreeNode]:
            nonlocal i

            if arr[i] == '#':
                i+=1
                return None

            node = TreeNode(int(arr[i]))
            i+=1
            
            node.left = reconstruct()
            node.right = reconstruct()

            return node
        
        return reconstruct()



# serialize
    # Create an array and have a preorder traversal with all the root values split by a comma. 