"""Arrow solid double bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '583b3a6d-5f81-55fe-aa87-3d6afa1f2e44'
SOURCE_PATH = 'icons-json/arrows/arrow solid double bottom_583b3a6d-5f81-55fe-aa87-3d6afa1f2e44.json'
AUTHOR = 'json_to_solo'

class ArrowSolidDoubleBottomArrows(Solo48):
    icon_id = 'arrow-solid-double-bottom-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'solid', 'double', 'bottom', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 44))
        self.add_line('sym-e1', (24, 44), (8, 34))
        self.add_line('sym-e2', (8, 34), (8, 25))
        self.add_line('sym-e3', (8, 25), (24, 33))
        self.add_line('sym-e4', (24, 33), (40, 25))
        self.add_line('sym-e5', (40, 25), (40, 34))
        self.add_line('sym-e6', (40, 34), (24, 44))
        self.add_line('sym-e7', (8, 4), (8, 13))
        self.add_line('sym-e8', (8, 13), (24, 23))
        self.add_line('sym-e9', (24, 23), (40, 13))
        self.add_line('sym-e10', (40, 13), (40, 4))
        self.add_line('sym-e11', (40, 4), (24, 12))
        self.add_line('sym-e12', (24, 12), (8, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', closed=True)
        self.add_contour('sym-c1', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', closed=True)
