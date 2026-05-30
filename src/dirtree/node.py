from .nodetype import NodeType

class Node(object):
    def __init__(self, name: str, node_type: NodeType):
        self.name = name
        self.type = node_type
        self.content: list[Node] = list()

    def add(self, el: 'Node'):
        self.content.append(el)