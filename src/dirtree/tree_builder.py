import os

from functools import reduce

from .node import Node
from .nodetype import NodeType

class TreeBuilder(object):
    def __init__(self, path):
        self._path = os.path.abspath(path)

    def _build_helper(self, path):
        folder_name = os.path.basename(path)
        
        root = Node(folder_name, 0, NodeType.DIR)

        for el in os.scandir(path):
            el_path = el.path
            el_size = os.path.getsize(el_path)

            if el.is_dir():
                sub_tree = self._build_helper(el_path)
                root.add(sub_tree)
                root.size += sub_tree.size
            else:
                root.add(Node(os.path.basename(el_path), el_size, NodeType.FILE))
                root.size += el_size

        root.content.sort(key=lambda x: x.size, reverse=True)

        return root

    def build(self):
        return self._build_helper(self._path)