#
# 名前ツリーのテスト
#
from unittest import TestCase

from src.nametree import NameNode, ANDNode, ORNode, NOTNode


class test_NameNode(TestCase):

    def test_equality(self):
        """名前ノードについては、文字列表現とLaTeX表現は同一
        """

        A = NameNode("A")

        self.assertEqual(A.str_repr, "A")
        self.assertEqual(A.str_repr, A.latex_repr)

    def test_basic_operation(self):
        """基本的な演算
        """
        A = NameNode("A")
        B = NameNode("B")

        A_AND_B = ANDNode(A, B)
        self.assertEqual(A_AND_B.str_repr, "A AND B")
        self.assertEqual(A_AND_B.latex_repr, "A \cap B")

        A_OR_B = ORNode(A, B)
        self.assertEqual(A_OR_B.str_repr, "A OR B")
        self.assertEqual(A_OR_B.latex_repr, "A \cup B")

        NOT_A = NOTNode(A)
        self.assertEqual(NOT_A.str_repr, "NOT A")
        self.assertEqual(NOT_A.latex_repr, "\bar{A}")

    def test_nested_operation(self):
        """複数の集合のネスト演算
        """
        A = NameNode("A")
        B = NameNode("B")
        C = NameNode("C")

        A_AND_B_OR_C = ORNode(ANDNode(A, B), C)
        self.assertEqual(A_AND_B_OR_C.str_repr, "(A AND B) OR C")
        self.assertEqual(A_AND_B_OR_C.latex_repr, "(A \cap B) \cup C")

        NOT_A_AND_NOT_B = ANDNode(NOTNode(A), NOTNode(B))
        self.assertEqual(NOT_A_AND_NOT_B.str_repr, "NOT A AND NOT B")
        self.assertEqual(NOT_A_AND_NOT_B.latex_repr, "\bar{A} \cap \bar{B}")
