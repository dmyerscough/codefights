#!/usr/bin/env python


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            self.left = self._add(self.left, value)
        elif value > self.value:
            self.right = self._add(self.right, value)

    def _add(self, parent, value):
        if parent is None:
            return Node(value)

        parent.add(value)
        return parent

    def remove(self, value):
        if value < self.value:
            self.left = self._remove(self.left, value)
        elif value > self.value:
            self.right = self._remove(self.right, value)
        else:
            if self.left is None:
                return self.right

            child = self.left
            while child.right:
                child = child.right

            childKey = child.value
            self.left = self._remove(self.left, childKey)
            self.value = childKey

        return self

    def _remove(self, parent, value):
        if parent:
            return parent.remove(value)
        return None


class Tree(object):

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add(value)

    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)

    def __contains__(self, value):
        node = self.root

        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True

        return False

    def breadth_first(self):
        level_description = {}
        level_count = 0

        current_level = [self.root]

        while current_level:
            next_level = list()

            for node in current_level:
                if level_description.get(level_count):
                    level_description[level_count] += node.value
                else:
                    level_description[level_count] = node.value

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level_count += 1
            current_level = next_level

        return level_description
