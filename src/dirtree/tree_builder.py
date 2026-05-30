import os

from .node import Node
from .nodetype import NodeType

class TreeBuilder(object):
    def __init__(self, path):
        self._path = os.path.abspath(path)

    def _build_helper(self, path):
        folder_name = os.path.basename(path)
        
        root = Node(folder_name, NodeType.DIR)

        for el in os.scandir(path):
            el_path = el.path

            if el.is_dir():
                root.add(self._build_helper(el_path))
            else:
                root.add(Node(os.path.basename(el_path), NodeType.FILE))

        return root

    def build(self):
        return self._build_helper(self._path)