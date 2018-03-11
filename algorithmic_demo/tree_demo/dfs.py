# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def presearch(self, tree, res):
        if tree is None:
            return
        else:
            res.append(tree.val)
        self.presearch(tree.left, res)
        self.presearch(tree.right, res)

    def depth_search(self, root):
        res = list()
        self.presearch(root, res)
        return res

    def stack_depth(self, root):
        """
        用栈来实现dfs
        """
        res = list()
        stx = [root]
        while len(stx) > 0:
            node = stx.pop()
            if node:
                res.append(node.val)
                stx.append(node.right)
                stx.append(node.left)
        return res

    def queue_bfs(self, root):
        res = list()
        queue = [root,]
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return res

    def bsearch(self, tree, res):
        if root:
            pass



    def breadth_search(self, root):
        res = list()
        self.breadth_search(root, res)



root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.left = TreeNode("F")
root.right.right = TreeNode("G")
print Solution().depth_search(root)
print Solution().stack_depth(root)
print Solution().queue_bfs(root)





