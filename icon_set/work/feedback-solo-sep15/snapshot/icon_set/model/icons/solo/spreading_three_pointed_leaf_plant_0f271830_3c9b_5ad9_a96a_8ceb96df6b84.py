"""Three pointed leaves above a tapered pot; shared-axis elliptic lobes inspired by Lucide sprout. Retains broad side leaves; omits no identity features."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f271830-3c9b-5ad9-a96a-8ceb96df6b84'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_0f271830-3c9b-5ad9-a96a-8ceb96df6b84.svg'
AUTHOR = 'gpt-6'


class SpreadingThreePointedLeafPlant(Solo48):
    icon_id = 'spreading-three-pointed-leaf-plant'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/plants"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # VRECT_XL centerline extremes (6,6)-(42,42).
        self.add_bezier('leaf-left-outer', (16, 32), *(((10.31845929, 31.05708721), (6, 22.37292966), (6, 12)),))
        self.add_arc("leaf-left-inner", (6,12), (18,20), radius_x=13, radius_y=8)
        self.add_bezier('leaf-centre-left', (18, 20), *(((18.63396337, 11.64319416), (21.14405636, 6), (24, 6)),))
        self.add_bezier('leaf-centre-right', (24, 6), *(((26.85594364, 6), (29.36603663, 11.64319416), (30, 20)),))
        self.add_arc("leaf-right-inner", (30,20), (42,12), radius_x=13, radius_y=8)
        self.add_bezier('leaf-right-outer', (42, 12), *(((42, 22.37292966), (37.68154071, 31.05708721), (32, 32)),))
        self.add_contour("foliage", "leaf-left-outer", "leaf-left-inner", "leaf-centre-left", "leaf-centre-right", "leaf-right-inner", "leaf-right-outer")
        self.add_polyline('mouth',(12,32),(16,32),(24,32),(32,32),(36,32))
        self.add_line("pot-right", (36,32), (34,42))
        self.add_bezier('bottom-right', (34, 42), *(((32.76239569, 42), (31.23760431, 42), (30, 42)),))
        self.add_line("bottom", (30,42), (18,42))
        self.add_bezier('bottom-left', (18, 42), *(((16.76239569, 42), (15.23760431, 42), (14, 42)),))
        self.add_line("pot-left", (14,42), (12,32))
        self.add_contour("pot", "pot-right", "bottom-right", "bottom", "bottom-left", "pot-left")
        self.relate("connect", "mouth", "pot")
        self.relate("connect", "foliage", "mouth")
