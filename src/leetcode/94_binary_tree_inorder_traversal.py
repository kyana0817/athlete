# from queue import SimpleQueue

# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self._lnode = None
#         self._rnode = None

#     @property
#     def lnode(self):
#         return self._lnode

#     @lnode.setter
#     def lnode(self, value):
#         if value is None: return
#         self._lnode = Node(value)

#     @property
#     def rnode(self):
#         return self._rnode

#     @rnode.setter
#     def rnode(self, value):
#         if value is None: return
#         self._rnode = Node(value)

#     def __str__(self):
#         if self.lnode is not None and self.rnode is not None:
#             return f"{self.lnode},{self.value},{self.rnode}"
#         if self.lnode is None:
#             return f"{self.value},{self.rnode}"
#         return f"{self.lnode},{self.value}"


# class Solution(object):
#     def binaryTreeInorderTraversal(self, root: list[int | None]) -> list[int]:
#         if len(root) <= 1:
#             return root

#         root_node = Node(root.pop(0))
#         task = SimpleQueue()
#         def parse(parent):
#             if parent is None: return
#             if len(root) > 0:
#                 parent.lnode = root.pop(0)
#             if len(root) > 0:
#                 parent.rnode = root.pop(0)
#             task.put(lambda: parse(parent.lnode))
#             task.put(lambda: parse(parent.rnode))

#         task.put(lambda: parse(root_node))

#         while len(root) > 0:
#             i = 0
#             qsize = task.qsize()
#             for _ in range(qsize):
#                 task.get()()

#         return [int(v) for v in str(root_node).split(',') if not v == 'None']


# if __name__ == "__main__":
#     solution = Solution()
#     assert solution.binaryTreeInorderTraversal([1,None,2,3]) == [1,3,2]
#     assert solution.binaryTreeInorderTraversal([1,2,3,4,5,None,8,None,None,6,7,9]) == [4,2,6,5,7,1,3,9,8]
#     assert solution.binaryTreeInorderTraversal([]) == []
#     assert solution.binaryTreeInorderTraversal([1]) == [1]    
#     print('All tests passed!')


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreeInorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        def parse(node: TreeNode | None):
            if node is None: return
            return f"{parse(node.left)},{node.val},{parse(node.right)}"
        p = parse(root)

        print([int(v) for v in p.split(',') if not v == 'None'])
        return [int(v) for v in p.split(',') if not v == 'None']

if __name__ == "__main__":
    solution = Solution()
    assert solution.binaryTreeInorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))) == [1,3,2]
    assert solution.binaryTreeInorderTraversal(TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, TreeNode(6, None, None), TreeNode(7, None, None))), TreeNode(3, None, TreeNode(8, TreeNode(9, None, None), None)))) == [4,2,6,5,7,1,3,9,8]
    # assert solution.binaryTreeInorderTraversal([]) == []
    # assert solution.binaryTreeInorderTraversal([1]) == [1]    
    print('All tests passed!')
