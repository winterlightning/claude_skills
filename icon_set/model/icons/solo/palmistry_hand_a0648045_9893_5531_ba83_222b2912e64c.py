"""An open palm with four rounded fingers, a left thumb, and two joined palmistry lines. Deliberately asymmetric for natural finger heights.

Construction: Lucide hand: shared finger walls, semicircular fingertips, broad rounded palm.
Keyshape SQUARE; centerline extremes are the visible bounds inset by 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0648045-9893-5531-ba83-222b2912e64c'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/palmistry_a0648045-9893-5531-ba83-222b2912e64c.svg'
AUTHOR = 'astra-chatgpt'


class PalmistryHand(Solo48):
    icon_id = 'palmistry-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('palmistry', 'palm reading', 'hand', 'fortune', 'divination', 'fate', 'lines', 'mystic')

    def build(self) -> None:
        self.add_line("index-outside", (14,28), (14,8))
        self.add_arc("index-tip", (14,8), (22,8), radius_x=4)
        self.add_line("middle-rise", (22,8), (22,6))
        self.add_arc("middle-tip", (22,6), (30,6), radius_x=4)
        self.add_line("middle-fall", (30,6), (30,8))
        self.add_arc("ring-tip", (30,8), (38,8), radius_x=4)
        self.add_line("ring-fall", (38,8), (38,12))
        self.add_arc("little-tip", (38,12), (46,12), radius_x=4)
        self.add_line("palm-right", (46,12), (46,30))
        self.add_arc("heel-right", (46,30), (30,46), radius_x=16)
        self.add_line("wrist", (30,46), (24,46))
        self.add_arc("heel-left", (24,46), (10,36), radius_x=14, radius_y=10)
        self.add_line("thumb-outside", (10,36), (2,24))
        self.add_arc("thumb-tip", (2,24), (10,24), radius_x=4)
        self.add_line("thumb-inside", (10,24), (14,28))
        self.add_contour("hand", "index-outside", "index-tip", "middle-rise", "middle-tip", "middle-fall", "ring-tip", "ring-fall", "little-tip", "palm-right", "heel-right", "wrist", "heel-left", "thumb-outside", "thumb-tip", "thumb-inside", closed=True)
        for name,x,y in (("index-crease",22,8),("middle-crease",30,8),("ring-crease",38,12)):
            self.add_line(name,(x,y),(x,20))
            self.relate("connect","hand",name)
        self.add_arc("heart-left", (22,28), (30,30), radius_x=17, sweep=False)
        self.add_arc("heart-right", (30,30), (38,28), radius_x=17, sweep=False)
        self.add_contour("heart-line", "heart-left", "heart-right")
        self.add_arc("life-line", (30,30), (24,38), radius_x=10)
        self.relate("connect","heart-line","life-line")
