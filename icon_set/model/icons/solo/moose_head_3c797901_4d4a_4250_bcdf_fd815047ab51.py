"""A moose with four upright antler tines and a blunt muzzle facing right, as in the supplied render. Tiny eye omitted.

Construction: No useful Lucide subject match found.
Keyshape SQUARE; centerline extremes are the visible bounds inset by 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c797901-4d4a-4250-bcdf-fd815047ab51'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/moose_3c797901-4d4a-4250-bcdf-fd815047ab51.svg'
AUTHOR = 'astra-chatgpt'


class MooseHead(Solo48):
    icon_id = 'moose-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('moose', 'elk', 'antlers', 'animal', 'wildlife', 'nordic', 'head', 'hunting')

    def build(self) -> None:
        self.add_line("antler-left-upright", (2,2), (2,10))
        self.add_arc("antler-left-bend", (2,10), (8,16), radius_x=6, sweep=False)
        for i, (a,b) in enumerate(zip([8,12,20,28,36], [12,20,28,36,40]), 1):
            self.add_line(f"antler-beam-{i}", (a,16), (b,16))
        self.add_arc("antler-right-bend", (40,16), (46,10), radius_x=6, sweep=False)
        self.add_line("antler-right-upright", (46,10), (46,2))
        self.add_contour("antlers", "antler-left-upright", "antler-left-bend", "antler-beam-1", "antler-beam-2", "antler-beam-3", "antler-beam-4", "antler-beam-5", "antler-right-bend", "antler-right-upright")
        self.add_line("tine-left", (12,16), (12,4))
        self.add_line("tine-right", (36,16), (36,4))
        self.add_line("forehead", (28,16), (38,26))
        self.add_arc("nose", (38,26), (30,38), radius_x=8)
        self.add_line("muzzle-under", (30,38), (26,36))
        self.add_line("neck", (26,36), (26,46))
        self.add_arc("throat", (26,46), (10,34), radius_x=16, radius_y=12)
        self.add_line("head-back", (10,34), (20,16))
        self.add_contour("head", "forehead", "nose", "muzzle-under", "neck", "throat", "head-back")
        self.relate("connect", "antlers", "head")
        self.relate("connect", "antlers", "tine-left")
        self.relate("connect", "antlers", "tine-right")
