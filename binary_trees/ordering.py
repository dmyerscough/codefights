#!/usr/bin/env python

from binary_tree import Tree


def inorder(node, res=None):
    if res is None:
        res = []

    if node is not None:
        inorder(node.left, res)
        res.append(node.value)
        inorder(node.right, res)

    return res


def preorder(node, res=None):
    if res is None:
        res = []

    if node is not None:
        res.append(node.value)
        preorder(node.left, res)
        preorder(node.right, res)

    return res


def postorder(node, res=None):
    if res is None:
        res = []

    if node is not None:
        postorder(node.left, res)
        postorder(node.right, res)
        res.append(node.value)

    return res


if __name__ == '__main__':

    tree = Tree()

    for i in [8, 3, 1, 6, 4, 7, 10, 14, 13]:
        tree.add(i)

    print "Inorder: ", inorder(tree.root)
    print "Preorder: ", preorder(tree.root)
    print "Postorder: ", postorder(tree.root)
