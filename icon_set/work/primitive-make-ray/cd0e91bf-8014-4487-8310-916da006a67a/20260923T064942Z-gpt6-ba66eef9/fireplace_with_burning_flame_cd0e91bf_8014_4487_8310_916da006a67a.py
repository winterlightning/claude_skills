"""A mantel fireplace with a small central flame.

Plan: one outer fire surround contains a second open firebox arch and a
connected flame. The side spacing is shared about x=24. Lucide heater
suggested the upright surround; Lucide flame informed the rising tongue.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cd0e91bf-8014-4487-8310-916da006a67a"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/mantel_cd0e91bf-8014-4487-8310-916da006a67a.svg"
AUTHOR = "gpt-6"


class FireplaceWithBurningFlame(Solo48):
    icon_id = "fireplace-with-burning-flame"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/home"
    aliases = ("mantel-fireplace",)
    keywords = ("fireplace", "hearth", "flame", "mantel")

    def build(self) -> None:
        self.add_polyline("surround", (4, 40), (4, 8), (44, 8),
                          (44, 40), (4, 40), closed=True)
        self.add_polyline("firebox", (12, 40), (12, 22), (16, 18),
                          (32, 18), (36, 22), (36, 40))
        self.add_polyline("flame", (24, 40), (20, 36), (21, 31),
                          (24, 26), (25, 31), (28, 35), (27, 38),
                          closed=True)
        self.relate("connect", "firebox", "surround")
        self.relate("connect", "flame", "surround")
