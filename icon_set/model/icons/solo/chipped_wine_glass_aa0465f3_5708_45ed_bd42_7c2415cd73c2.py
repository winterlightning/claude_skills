from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa0465f3-5708-45ed-bd42-7c2415cd73c2'
SOURCE_PATH = 'pictographic-primitives/shipping/fragile chip_aa0465f3-5708-45ed-bd42-7c2415cd73c2.svg'
AUTHOR = 'gpt-6-astra'


class ChippedWineGlass(Solo48):
    icon_id = 'chipped-wine-glass'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    categories = ("primitives", "shipping")
    aliases = ()
    keywords = ('glass', 'wine', 'fragile', 'chip', 'broken', 'stemware')

    def build(self) -> None:
        # Vertical centerlines (8,4)-(40,44); asymmetric fracture and detached chip.
        self.add_polyline("rim", (16,20), (24,13), (25,4), (37,4), (40,20))
        self.add_arc("bowl-right", (40,20), (28,32), radius_x=12)
        self.add_arc("bowl-left", (28,32), (16,20), radius_x=12)
        self.add_contour("bowl", "bowl-right", "bowl-left")
        self.relate("connect", "rim", "bowl")
        self.add_line("stem", (28,32), (28,44))
        self.add_polyline("foot", (18,44), (28,44), (38,44))
        self.relate("connect", "bowl", "stem")
        self.relate("connect", "stem", "foot")
        self.add_polyline("chip", (8,4), (15,4), (12,10))
