#
#
#
from .base import NodeBase


class NameNode(NodeBase):
    """集合名ノード
    """

    def __init__(self, set_name: str) -> None:
        """集合名を引数に名前ノードを初期化

        Args:
            set_name (str): 集合名
        """
        self.set_name = set_name

    @property
    def is_monolithic(self) -> bool:
        return True

    @property
    def str_repr(self) -> str:
        return self.set_name

    @property
    def latex_repr(self) -> str:
        return self.set_name
