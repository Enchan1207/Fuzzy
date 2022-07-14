#
# 集合演算ノード
#
from .base import NodeBase


class ANDNode(NodeBase):
    """ANDノード
    """

    def __init__(self, node: NodeBase, node_b: NodeBase) -> None:
        """複数のノードから演算ノードを初期化

        Args:
            node (NodeBase): 左辺
            node_b (NodeBase): 右辺
        """
        self.node = node
        self.node_b = node_b

    @property
    def is_monolithic(self) -> bool:
        return False

    @property
    def str_repr(self) -> str:
        node_repr = self.node.str_repr if self.node.is_monolithic else f"({self.node.str_repr})"
        node_b_repr = self.node_b.str_repr if self.node_b.is_monolithic else f"({self.node_b.str_repr})"
        return f"{node_repr} AND {node_b_repr}"

    @property
    def latex_repr(self) -> str:
        node_repr = self.node.latex_repr if self.node.is_monolithic else f"({self.node.latex_repr})"
        node_b_repr = self.node_b.latex_repr if self.node_b.is_monolithic else f"({self.node_b.latex_repr})"
        return f"{node_repr} \cap {node_b_repr}"


class ORNode(NodeBase):
    """ ORノード
    """

    def __init__(self, node: NodeBase, node_b: NodeBase) -> None:
        """複数のノードから演算ノードを初期化

        Args:
            node (NodeBase): 左辺
            node_b (NodeBase): 右辺
        """
        self.node = node
        self.node_b = node_b

    @property
    def is_monolithic(self) -> bool:
        return False

    @property
    def str_repr(self) -> str:
        node_repr = self.node.str_repr if self.node.is_monolithic else f"({self.node.str_repr})"
        node_b_repr = self.node_b.str_repr if self.node_b.is_monolithic else f"({self.node_b.str_repr})"
        return f"{node_repr} OR {node_b_repr}"

    @property
    def latex_repr(self) -> str:
        node_repr = self.node.latex_repr if self.node.is_monolithic else f"({self.node.latex_repr})"
        node_b_repr = self.node_b.latex_repr if self.node_b.is_monolithic else f"({self.node_b.latex_repr})"
        return f"{node_repr} \cup {node_b_repr}"


class NOTNode(NodeBase):
    """ NOTノード
    """

    def __init__(self, node: NodeBase) -> None:
        """単一のノードから演算ノードを初期化

        Args:
            node (NodeBase): ノード
        """
        self.node = node

    @property
    def is_monolithic(self) -> bool:
        return True

    @property
    def str_repr(self) -> str:
        node_repr = self.node.str_repr if self.node.is_monolithic else f"({self.node.str_repr})"
        return f"NOT {node_repr}"

    @property
    def latex_repr(self) -> str:
        node_repr = self.node.latex_repr if self.node.is_monolithic else f"({self.node.latex_repr})"
        return r"\overline{" + node_repr + r"}"
