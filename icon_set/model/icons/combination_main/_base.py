"""Combination mains use solo geometry rules in their own family and folder."""
from ..family import FamilyIcon
from ...keyshapes import Keyshape


class CombinationMain48(FamilyIcon):
    family = "combination_main"
    icon_id: str = ""
    keyshape: Keyshape = Keyshape.SQUARE
    semantic_role: str = "MAIN"
    semantic_kind: str = "noun"
    category: str = "objects"
    aliases: tuple[str, ...] = ()
    keywords: tuple[str, ...] = ()
