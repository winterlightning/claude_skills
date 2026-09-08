"""A flared-neck amphora with paired loop handles and a flat foot; Lucide amphora informs the paired construction."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '767e1228-a1ba-5656-92aa-ecb41051073a'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/vase_767e1228-a1ba-5656-92aa-ecb41051073a.svg'
SOURCE_REFERENCES = (('e30e73e8-cfbc-5e50-8790-a60a3cd980aa', 'pictographic-primitives/culture/batch-01/vase_e30e73e8-cfbc-5e50-8790-a60a3cd980aa.svg'),)


class HandledAmphoraVase(Solo48):
    icon_id = 'handled-amphora-vase'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('vase', 'amphora', 'greek', 'pottery', 'handles', 'ceramic', 'vessel', 'antique')

    def build(self) -> None:
        # VRECT_XL: visible extremes (3, 0, 45, 48); centerlines inset 2.
        self.add_line("lip-neck-left-1", (14,2), (18,10))
        self.add_line("lip-neck-left-2", (18,10), (18,14))
        self.add_arc("shoulder-left", (18,14), (12,26), radius_x=6, radius_y=12, sweep=False)
        self.add_arc("body-left", (12,26), (24,46), radius_x=12, radius_y=20, sweep=False)
        self.add_arc("body-right", (24,46), (36,26), radius_x=12, radius_y=20, sweep=False)
        self.add_arc("shoulder-right", (36,26), (30,14), radius_x=6, radius_y=12, sweep=False)
        self.add_line("neck-lip-right-1", (30,14), (30,10))
        self.add_line("neck-lip-right-2", (30,10), (34,2))
        self.add_line("neck-lip-right-3", (34,2), (14,2))
        self.add_contour("outline", "lip-neck-left-1", "lip-neck-left-2", "shoulder-left", "body-left", "body-right", "shoulder-right", "neck-lip-right-1", "neck-lip-right-2", "neck-lip-right-3", closed=True)
        self.add_arc("handle-left-top", (18,10), (5,18), radius_x=13, radius_y=8, sweep=False)
        self.add_arc("handle-left-bottom", (5,18), (12,26), radius_x=7, radius_y=8, sweep=False)
        self.add_contour("handle-left", "handle-left-top", "handle-left-bottom")
        self.add_arc("handle-right-top", (30,10), (43,18), radius_x=13, radius_y=8)
        self.add_arc("handle-right-bottom", (43,18), (36,26), radius_x=7, radius_y=8)
        self.add_contour("handle-right", "handle-right-top", "handle-right-bottom")
        self.add_polyline("foot", (18,46), (24,46), (30,46))
        self.relate("connect", "outline", "handle-left")
        self.relate("connect", "outline", "handle-right")
        self.relate("connect", "outline", "foot")
