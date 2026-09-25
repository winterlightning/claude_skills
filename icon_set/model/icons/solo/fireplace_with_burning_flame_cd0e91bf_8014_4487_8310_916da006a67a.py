"""mantel: standalone repair of supplied reference.

Plan: Wide fire surround. Keyshape HRECT_L.
Reduction: Omitted secondary inset firebox arch and inner flame tongue; retained surround and central flame.
Construction references: local Lucide originals and atomic-debug: flame.

All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "cd0e91bf-8014-4487-8310-916da006a67a"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/mantel_cd0e91bf-8014-4487-8310-916da006a67a.svg"
AUTHOR = "gpt-6"


class FireplaceWithBurningFlame(Solo48):
    icon_id = 'fireplace-with-burning-flame'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("mantel-fireplace",)
    keywords = ("fireplace", "hearth", "flame", "mantel")

    def build(self) -> None:
        self.add_polyline("surround", (4, 40), (4, 8), (44, 8),
                          (44, 40), (4, 40), closed=True)
        # One generously open fire chamber; secondary inset arch omitted.
        self.add_bezier("flame", (24, 31),
            ((12, 31), (18, 23), (24, 17)),
            ((24, 23), (36, 31), (24, 31)))
