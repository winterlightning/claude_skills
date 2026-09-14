"""Arrow solid double right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cbb50c7c-d449-519f-8f1e-944105fecb9d'
SOURCE_PATH = 'icons-json/arrows/arrow solid double right_cbb50c7c-d449-519f-8f1e-944105fecb9d.json'
AUTHOR = 'json_to_solo'

class ArrowSolidDoubleRightArrows(Solo48):
    icon_id = 'arrow-solid-double-right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'solid', 'double', 'right', 'arrows')

    def build(self):
        self.add_line('sym-e0', (44, 24), (44, 24))
        self.add_line('sym-e1', (44, 24), (34, 40))
        self.add_line('sym-e2', (34, 40), (25, 40))
        self.add_line('sym-e3', (25, 40), (33, 24))
        self.add_line('sym-e4', (33, 24), (25, 8))
        self.add_line('sym-e5', (25, 8), (34, 8))
        self.add_line('sym-e6', (34, 8), (44, 24))
        self.add_line('sym-e7', (4, 40), (13, 40))
        self.add_line('sym-e8', (13, 40), (23, 24))
        self.add_line('sym-e9', (23, 24), (13, 8))
        self.add_line('sym-e10', (13, 8), (4, 8))
        self.add_line('sym-e11', (4, 8), (12, 24))
        self.add_line('sym-e12', (12, 24), (4, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', closed=True)
        self.add_contour('sym-c1', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', closed=True)
