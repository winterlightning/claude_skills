"""Decision (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d2412b5-287b-4962-8979-8680db7f486f'
SOURCE_PATH = 'icons-json/design/decision_3d2412b5-287b-4962-8979-8680db7f486f.json'
AUTHOR = 'json_to_solo'

class DecisionDesign(Solo48):
    icon_id = 'decision-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('decision', 'design')

    def build(self):
        self.add_line('sym-e0', (44, 24), (24, 40))
        self.add_bezier('sym-e1', (24, 40), ((23.7, 40), (23.3, 40), (23, 40)))
        self.add_line('sym-e2', (23, 40), (4, 24))
        self.add_line('sym-e3', (4, 24), (23, 8))
        self.add_bezier('sym-e4', (23, 8), ((23.3, 8), (23.7, 8), (24, 8)))
        self.add_line('sym-e5', (24, 8), (44, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', closed=True)
