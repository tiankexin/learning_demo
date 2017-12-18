# -*- coding: utf-8 -*-

"""
用python实现一些基本的数据结构
"""

# 单向链表


class Node(object):

    def __init__(self, data):
        self.value = data
        self.next_n = None


class LinkList(object):

    def __init__(self, node):
        self.head = node
        self.tail = node

    def add_node(self, node):
        self.tail.next_n = node
        self.tail = node

    def view(self):
        node = self.head
        link_str = ''
        while node is not None:
            if node.next_n is not None:
                link_str += str(node.value) + '-->'
            else:
                link_str += str(node.value)
            node = node.next_n
        print "Link str:" + link_str
        return link_str

    def lenth(self):
        node = self.head
        count = 1
        while node.next_n is not None:
            count += 1
            node = node.next_n
        print "Link count:" + str(count)
        return count

    def delete_node(self, index):
        if index + 1 > self.lenth():
            raise IndexError("out range")
        num = 0
        node = self.head
        while True:
            if num == index - 1:
                break
            node = node.next_n
            num += 1
        tmp_node = node.next_n
        node.next_n = node.next_n.next_n
        return tmp_node

    def find_node(self, index):
        if index + 1 > self.lenth():
            raise IndexError("out range")
        num = 0
        node = self.head
        while True:
            if num == index:
                break
            node = node.next_n
            num += 1
        return node.value


node1 = Node(10)
node2 = Node('dec')
node3 = Node(1010)
node4 = Node('bin')
node5 = Node(12)
node6 = Node('oct')
node7 = Node('A')
node8 = Node('hex')

linklist = LinkList(node1)
linklist.add_node(node2)
linklist.add_node(node3)
linklist.add_node(node4)
linklist.add_node(node5)
linklist.add_node(node6)
linklist.add_node(node7)
linklist.add_node(node8)

linklist.view()
linklist.lenth()
linklist.delete_node(1)
linklist.view()
find_node = linklist.find_node(6)
print find_node

class TreeNode(object):
    def __init__(self, x, leftNode=None, rightNode=None):
        self.val = x
        self.left = leftNode
        self.right = rightNode

    def __str__(self):
        return str(self.val)


class Solution(object):
    def invert_tree(self, node):
        """
        :type node: TreeNode
        :rtype: TreeNode
        """
        if node:
            node.left, node.right = node.right, node.left
            if node.left:
                node.left = self.invert_tree(node.left)
            if node.right:
                node.right = self.invert_tree(node.right)
        return node


def print_tree(node=None, is_child=False, deep=3):
    if not node and is_child:
        return

    if not is_child:
        print node

    if not node.left and not node.right:
        return

    print "%s> " % node, node.left, node.right
    print_tree(node.left, is_child=True)
    print_tree(node.right, is_child=True)


if __name__ == '__main__':
    root = TreeNode(
        4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9))
    )

    print_tree(root)
    print '====='
    solution = Solution()
    invert_node = solution.invert_tree(root)
    print_tree(invert_node)