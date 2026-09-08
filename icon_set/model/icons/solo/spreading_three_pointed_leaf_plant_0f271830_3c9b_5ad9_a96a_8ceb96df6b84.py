"""Three pointed leaves above a tapered pot; shared-axis elliptic lobes inspired by Lucide sprout. Retains broad side leaves; omits no identity features."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f271830-3c9b-5ad9-a96a-8ceb96df6b84'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_0f271830-3c9b-5ad9-a96a-8ceb96df6b84.svg'
AUTHOR = 'gpt-6'


class SpreadingThreePointedLeafPlant(Solo48):
    icon_id = 'spreading-three-pointed-leaf-plant'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/plants"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # VRECT_XL centerline extremes (5,2)-(43,46).
        self.add_arc("leaf-left-outer", (16,32), (5,12), radius_x=11, radius_y=20)
        self.add_arc("leaf-left-inner", (5,12), (18,20), radius_x=13, radius_y=8)
        self.add_arc("leaf-centre-left", (18,20), (24,2), radius_x=6, radius_y=18)
        self.add_arc("leaf-centre-right", (24,2), (30,20), radius_x=6, radius_y=18)
        self.add_arc("leaf-right-inner", (30,20), (43,12), radius_x=13, radius_y=8)
        self.add_arc("leaf-right-outer", (43,12), (32,32), radius_x=11, radius_y=20)
        self.add_contour("foliage", "leaf-left-outer", "leaf-left-inner", "leaf-centre-left", "leaf-centre-right", "leaf-right-inner", "leaf-right-outer")
        self.add_polyline("mouth", (12,32), (24,32), (36,32))
        self.add_line("pot-right", (36,32), (34,42))
        self.add_arc("bottom-right", (34,42), (30,46), radius_x=4)
        self.add_line("bottom", (30,46), (18,46))
        self.add_arc("bottom-left", (18,46), (14,42), radius_x=4)
        self.add_line("pot-left", (14,42), (12,32))
        self.add_contour("pot", "pot-right", "bottom-right", "bottom", "bottom-left", "pot-left")
        self.relate("connect", "mouth", "pot")
        self.relate("connect", "foliage", "mouth")
