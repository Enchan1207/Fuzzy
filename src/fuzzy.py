#
# 離散ファジィ集合
#

from __future__ import annotations
from functools import reduce
from typing import Dict, List


class Fuzzy:
    """離散ファジィ集合
    """

    def __init__(self, base: List[int], grade: Dict[int, float], name) -> None:
        """ファジィ集合の初期化

        Args:
            base (List[int]): 台集合
            grade (Dict[int, float]): グレード値
            name: 集合名
        """

        self.base = base
        self.name = name
        self._is_monolithic = True  # 単体かどうか

        # バリデーション
        if list(filter(lambda i: i < 0.0 or i > 1.0, grade.values())) != []:
            raise ValueError("Value of grade must be between 0.0 to 1.0")

        # グレード値辞書を全射化(0.0/nは省略ableだが、内部では省略しないで全部持つ)
        self.grade: Dict[int, float] = {}
        for key in self.base:
            self.grade[key] = grade.get(key) or 0.0

    @staticmethod
    def parse_from(base: List[int], repr: str, name: str) -> Fuzzy:
        """台集合と文字列表現からファジィ集合を生成します.

        Args:
            base (List[int]): 台集合
            repr (str): 文字列表現(表現1)
            name: 集合名

        Note:
            文字列表現は以下のフォーマットである必要があります:  
            `グレード値/キー,グレード値/キー,...`

        Returns:
            Fuzzy: 生成結果
        """

        grade: Dict[int, float] = reduce(lambda a, b: a | b, [{int(l[1]): float(l[0])} for l in [
            i.split("/") for i in repr.split(",")]])
        return Fuzzy(base, grade, name)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(\n\tname:{self.name}\n\t{self.base}\n\t{self.grade}\n)"

    def __and__(self, other: Fuzzy) -> Fuzzy:
        if self.base != other.base:
            raise ValueError("Base of fuzzy set must be same size")

        # 小さい方を抽出
        result: Dict[int, float] = {}
        for key, value_self, value_other in zip(self.grade.keys(), self.grade.values(), other.grade.values()):
            result[key] = value_self if value_self < value_other else value_other

        # 名前の生成
        # モノリシックな集合でなければカッコをつける
        self_newname = self.name if self._is_monolithic else f"({self.name})"
        other_newname = other.name if other._is_monolithic else f"({other.name})"
        newname = self_newname + " AND " + other_newname

        new_fuzzy = Fuzzy(self.base, result, newname)
        new_fuzzy._is_monolithic = False
        return new_fuzzy

    def __or__(self, other: Fuzzy) -> Fuzzy:
        if self.base != other.base:
            raise ValueError("Base of fuzzy set must be same size")

        # 大きい方を抽出
        result: Dict[int, float] = {}
        for key, value_self, value_other in zip(self.grade.keys(), self.grade.values(), other.grade.values()):
            result[key] = value_self if value_self > value_other else value_other

        # 名前の生成
        # モノリシックな集合でなければカッコをつける
        self_newname = self.name if self._is_monolithic else f"({self.name})"
        other_newname = other.name if other._is_monolithic else f"({other.name})"
        newname = self_newname + " OR " + other_newname

        new_fuzzy = Fuzzy(self.base, result, newname)
        new_fuzzy._is_monolithic = False
        return new_fuzzy

    @property
    def inversed(self) -> Fuzzy:
        result: Dict[int, float] = {}
        for key, value in self.grade.items():
            result[key] = 1.0 - value

        # 名前の生成
        # モノリシックな集合でなければカッコをつける
        self_newname = self.name if self._is_monolithic else f"({self.name})"
        newname = "NOT " + self_newname

        new_fuzzy = Fuzzy(self.base, result, newname)
        new_fuzzy._is_monolithic = False
        return new_fuzzy

    @property
    def set_repr(self) -> str:
        # グレード値が0でないもののみ列挙
        return ','.join([f"{item[1]:.1f}/{item[0]}" for item in list(filter(lambda n: n[1] > 0.0, self.grade.items()))])
