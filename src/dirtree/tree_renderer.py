import logging

from .node import Node
from .nodetype import NodeType
from .text_modifier import TextModifier
from .building_block import BuildingBlock
from .size_unit import SizeUnit

_logger = logging.getLogger(__name__)

class TreeRenderer(object):
    def __init__(self, tree):
        self._tree = tree
        self._completed_levels = set()

    def _indentation(self, level):
        _logger.debug(f"Computing indentation for level {level}")

        if level == 0:
            return "  " * level

        s = ""

        for i in range(level - 1):
            s = f"{s}   "
            
            if i not in self._completed_levels:
                _logger.debug(f"Level {level} is not completed yet. Add a vertical line")
                s = f"{s}{BuildingBlock.V_LINE.value}"
            else:
                s = f"{s} "

        s = f"{s}   "

        _logger.debug(f"Finished computing indentation for level {level}. Indentation:{s}")

        return s

    def _render_helper(self, tree: Node, level):
        _logger.debug(f"Rendering node {tree.name} at level {level}")
        
        s = ""

        if tree.type == NodeType.FILE:
            s = f"{s}{TextModifier.ITALIC.value}"

        tree_size, size_unit = SizeUnit.compute_unit(tree.size)
        s = f"{s}{tree.name} ({tree_size} {size_unit.value}){TextModifier.NORMAL.value}"

        print(s)

        content_len = len(tree.content)
        i = 0

        _logger.debug(f"Node {tree.name} contains {content_len} elements.\nRecursively render those as well")

        content_indentation = self._indentation(level + 1)
        while i < content_len:
            s = content_indentation

            if i == content_len - 1:
                line = BuildingBlock.BOT_LEFT_ANGLE.value
                self._completed_levels.add(level)
            else:
                line = BuildingBlock.H_TSHAPE_R.value

            s = f"{s}{line}{BuildingBlock.H_LINE.value}"
            print(s, end=" ")
            self._render_helper(tree.content[i], level + 1)
            i += 1

        _logger.debug(f"Finished rendering node {tree.name}")
        # Reset current level indentation
        self._completed_levels.discard(level)

    def render(self):
        self._render_helper(self._tree, 0)