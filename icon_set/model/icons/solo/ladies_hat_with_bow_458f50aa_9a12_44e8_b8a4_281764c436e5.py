"""A domed ladies hat with broad brim and right-side bow. Lucide hat-glasses informs crown and brim; asymmetry preserves the bow placement."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '458f50aa-9a12-44e8-b8a4-281764c436e5'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/hat lady_458f50aa-9a12-44e8-b8a4-281764c436e5.svg'
AUTHOR = 'astra-chatgpt'

class LadiesHatWithBow(Solo48):
    icon_id = 'ladies-hat-with-bow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('ladies', 'hat', 'with', 'bow')

    def build(self) -> None:
        # Centerline extremes (2,8)-(46,40).
        self.add_arc("crown", (8,26), (36,26), radius_x=14, radius_y=18)
        self.add_line("brim-left", (8,26), (2,34))
        self.add_arc("brim-lower-left", (2,34), (24,40), radius_x=22, radius_y=6, sweep=False)
        self.add_arc("brim-lower-right", (24,40), (46,34), radius_x=22, radius_y=6, sweep=False)
        self.add_line("brim-right", (46,34), (40,28))
        self.add_contour("brim", "brim-left", "brim-lower-left", "brim-lower-right", "brim-right")
        self.add_line("band", (8,26), (25,26))
        self.add_polyline("bow-left", (35,26), (25,20), (25,26), (25,32), closed=True)
        self.add_polyline("bow-right", (35,26), (45,20), (45,32), closed=True)
        self.relate("connect", "crown", "brim")
        self.relate("connect", "crown", "band")
        self.relate("connect", "brim", "band")
        self.relate("connect", "bow-left", "bow-right")
        self.relate("connect", "band", "bow-left")
