# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class Stack(object):

    def __init__(self):
        self._container = []

    @property
    def is_empty(self):
        return len(self._container) == 0

    def push(self, element):
        """
        Add a new element to the stack
        :param element: the element you want to add
        :return: None
        """
        self._container.append(element)

    def top(self):
        """
        Get the top element of the stack
        :return: top element
        """
        if self.is_empty:
            return None
        return self._container[-1]

    def pop(self):
        return None if self.is_empty else self._container.pop(-1)

    def clear(self):
        """
        We'll make an empty stack
        :return: self
        """
        del self._container[:]
        return self

    def size(self):
        return len(self._container)
