#
# 集合名ノードの基底クラス
#
from abc import ABC, abstractmethod


class NodeBase(ABC):
    """集合名ノード
    """

    @property
    @abstractmethod
    def is_monolithic(self) -> bool:
        """モノリシックかどうか(演算後のノードか)
        """
        pass

    @property
    @abstractmethod
    def str_repr(self) -> str:
        """ノードのプレーンテキスト表現.
        """
        pass

    @property
    @abstractmethod
    def latex_repr(self) -> str:
        """ノードのLaTeX表現.
        """
        pass
