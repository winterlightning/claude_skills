"""A handleless narrow-necked vase with a rounded belly and flat base.

Construction: Lucide amphora: mirrored neck-to-belly flow; handles excluded because the supplied vase has none.
Keyshape VRECT_L; centerline extremes are the visible bounds inset by 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8bd2444f-5efb-508a-8576-7be7a1ed2a03'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/vase_8bd2444f-5efb-508a-8576-7be7a1ed2a03.svg'


class NarrowNeckedVase(Solo48):
    icon_id = 'narrow-necked-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('vase', 'pottery', 'ceramic', 'vessel', 'decorative', 'flowers', 'antique', 'urn')

    def build(self) -> None:
        self.add_line("lip", (16,2), (32,2))
        self.add_line("neck-right", (32,2), (32,10))
        self.add_arc("flare-right", (32,10), (36,20), radius_x=14, sweep=False)
        self.add_arc("belly-upper-right", (36,20), (40,32), radius_x=20)
        self.add_arc("base-right", (40,32), (26,46), radius_x=14)
        self.add_line("base", (26,46), (22,46))
        self.add_arc("base-left", (22,46), (8,32), radius_x=14)
        self.add_arc("belly-upper-left", (8,32), (12,20), radius_x=20)
        self.add_arc("flare-left", (12,20), (16,10), radius_x=14, sweep=False)
        self.add_line("neck-left", (16,10), (16,2))
        self.add_contour("vase", "lip", "neck-right", "flare-right", "belly-upper-right", "base-right", "base", "base-left", "belly-upper-left", "flare-left", "neck-left", closed=True)
