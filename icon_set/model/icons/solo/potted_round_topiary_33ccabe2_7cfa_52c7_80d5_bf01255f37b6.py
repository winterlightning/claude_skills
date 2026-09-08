"""Round topiary crown on a straight trunk and trapezoidal pot. Tiny scallops reduced to a smooth circle; Lucide flower-2 informs simple crown/stem attachment."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33ccabe2-7cfa-52c7-80d5-bf01255f37b6'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_33ccabe2-7cfa-52c7-80d5-bf01255f37b6.svg'
AUTHOR = 'gpt-6'


class PottedRoundTopiary(Solo48):
    icon_id = 'potted-round-topiary'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/plants"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # VRECT_M extremes (11,2)-(37,46).
        self.add_arc("crown-top-left", (11,15), (24,2), radius_x=13)
        self.add_arc("crown-top-right", (24,2), (37,15), radius_x=13)
        self.add_arc("crown-bottom-right", (37,15), (24,28), radius_x=13)
        self.add_arc("crown-bottom-left", (24,28), (11,15), radius_x=13)
        self.add_contour("crown", "crown-top-left", "crown-top-right", "crown-bottom-right", "crown-bottom-left", closed=True)
        self.add_line("trunk", (24,28), (24,36))
        self.add_polyline("pot", (13,36), (24,36), (35,36), (32,46), (16,46), closed=True)
        self.relate("connect", "crown", "trunk")
        self.relate("connect", "trunk", "pot")
