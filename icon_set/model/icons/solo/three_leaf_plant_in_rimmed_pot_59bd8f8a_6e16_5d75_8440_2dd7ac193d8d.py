"""Three long leaves with visible shared seams and a projecting pot rim. Lucide sprout informs elliptic leaves; mirrored leaves preserve the source crown."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59bd8f8a-6e16-5d75-8440-2dd7ac193d8d'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_59bd8f8a-6e16-5d75-8440-2dd7ac193d8d.svg'
AUTHOR = 'gpt-6'


class ThreeLeafPlantInRimmedPot(Solo48):
    icon_id = 'three-leaf-plant-in-rimmed-pot'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/plants"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # VRECT_XL centerline extremes (5,2)-(43,46).
        self.add_arc("leaf-left-outer", (16,30), (5,12), radius_x=11, radius_y=18)
        self.add_arc("leaf-left-inner", (5,12), (18,20), radius_x=13, radius_y=8)
        self.add_arc("leaf-centre-left", (18,20), (24,2), radius_x=6, radius_y=18)
        self.add_arc("leaf-centre-right", (24,2), (30,20), radius_x=6, radius_y=18)
        self.add_arc("leaf-right-inner", (30,20), (43,12), radius_x=13, radius_y=8)
        self.add_arc("leaf-right-outer", (43,12), (32,30), radius_x=11, radius_y=18)
        self.add_contour("foliage", "leaf-left-outer", "leaf-left-inner", "leaf-centre-left", "leaf-centre-right", "leaf-right-inner", "leaf-right-outer")
        self.add_polyline("rim", (10,30), (24,30), (38,30), (38,36), (34,36), (14,36), (10,36), closed=True)
        self.add_polyline("pot", (14,36), (16,46), (32,46), (34,36))
        self.relate("connect", "rim", "pot")
        self.relate("connect", "foliage", "rim")
        self.add_line("left-leaf-seam", (18,20), (24,30))
        self.add_line("right-leaf-seam", (30,20), (24,30))
        self.relate("connect", "left-leaf-seam", "foliage")
        self.relate("connect", "right-leaf-seam", "foliage")
        self.relate("connect", "left-leaf-seam", "right-leaf-seam")
        self.relate("connect", "left-leaf-seam", "rim")
        self.relate("connect", "right-leaf-seam", "rim")
