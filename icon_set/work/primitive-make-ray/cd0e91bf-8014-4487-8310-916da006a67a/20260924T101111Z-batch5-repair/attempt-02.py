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
        # One generously open fire chamber; secondary inset arch omitted.
        self.add_bezier("flame", (24, 32),
            ((12, 32), (18, 23), (24, 17)),
            ((24, 23), (36, 32), (24, 32)))
