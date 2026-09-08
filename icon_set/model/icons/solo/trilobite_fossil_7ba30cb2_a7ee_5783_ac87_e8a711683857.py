"""A domed trilobite shield and tapering segmented body; bounds (5,2)-(43,46).

Construction reference: Lucide bug: bilateral shell organization; source supplies broad shield and transverse segments.
Centerline extremes are the declared keyshape's exact bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ba30cb2-a7ee-5783-ac87-e8a711683857'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/trilobite fossil shell_7ba30cb2-a7ee-5783-ac87-e8a711683857.svg'


class TrilobiteFossil(Solo48):
    icon_id = 'trilobite-fossil'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('trilobite', 'fossil', 'prehistoric', 'palaeontology', 'shell', 'arthropod', 'ancient', 'museum')

    def build(self) -> None:
        self.add_arc("head-left", (5, 21), (24, 2), radius_x=19)
        self.add_arc("head-right", (24, 2), (43, 21), radius_x=19)
        self.add_line("head-base-right", (43, 21), (37, 21))
        self.add_line("head-base-middle", (37, 21), (11, 21))
        self.add_line("head-base-left", (11, 21), (5, 21))
        self.add_contour("head", "head-left", "head-right", "head-base-right", "head-base-middle", "head-base-left", closed=True)
        self.add_arc("head-ridge", (19, 12), (29, 12), radius_x=7, radius_y=3)
        self.add_line("body-r1", (37, 21), (34, 30))
        self.add_line("body-r2", (34, 30), (30, 38))
        self.add_arc("tail-right", (30, 38), (24, 46), radius_x=6, radius_y=8)
        self.add_arc("tail-left", (24, 46), (18, 38), radius_x=6, radius_y=8)
        self.add_line("body-l2", (18, 38), (14, 30))
        self.add_line("body-l1", (14, 30), (11, 21))
        self.add_contour("body", "body-r1", "body-r2", "tail-right", "tail-left", "body-l2", "body-l1")
        self.relate("connect", "head", "body")
        self.add_line("segment-top", (14, 30), (34, 30))
        self.add_line("segment-bottom", (18, 38), (30, 38))
        self.relate("connect", "body", "segment-top")
        self.relate("connect", "body", "segment-bottom")
        self.add_line("leg-left", (14, 30), (7, 34))
        self.add_line("leg-right", (34, 30), (41, 34))
        for leg in ("leg-left", "leg-right"):
            self.relate("connect", "body", leg)
            self.relate("connect", "segment-top", leg)
