"""One angular lightning flash.

Plan: a single closed zigzag silhouette with two open side notches.
The directional asymmetry preserves the reference. Lucide zap supplied the
continuous six-point construction, redrawn on the SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "223231a7-c760-4c40-ba86-2b1878f06e12"
SOURCE_PATH = "pictographic-primitives/_uncategorized_25/lighting_223231a7-c760-4c40-ba86-2b1878f06e12.svg"
AUTHOR = "gpt-6"


class LightningBoltSymbol(Solo48):
    icon_id = "lightning-bolt-symbol"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/weather"
    aliases = ("flash", "electric-bolt")
    keywords = ("lightning", "electricity", "energy", "thunder")

    def build(self) -> None:
        # VRECT_L centerline extremes: left 8, right 40, top 4, bottom 44.
        self.add_polyline("bolt", (32, 4), (8, 26), (22, 26),
                          (14, 44), (40, 20), (26, 20), closed=True)
