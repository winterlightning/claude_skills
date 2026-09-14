"""Delay (diagrams), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'caeb15c5-d005-4c7a-bdb2-16c3ef5f037a'
SOURCE_PATH = 'icons-json/diagrams/delay_caeb15c5-d005-4c7a-bdb2-16c3ef5f037a.json'
AUTHOR = 'json_to_solo'

class DelayDiagrams(Solo48):
    icon_id = 'delay-diagrams'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('delay', 'diagrams')

    def build(self):
        self.add_line('sym-e0', (4, 8), (4, 24))
        self.add_line('sym-e1', (4, 24), (4, 40))
        self.add_line('sym-e2', (4, 40), (27, 40))
        self.add_bezier('sym-e3', (27, 40), ((28.036, 40), (28.982, 40), (30, 40)))
        self.add_bezier('sym-e4', (30, 40), ((37.473, 38.476), (44, 32.377), (44, 25)))
        self.add_bezier('sym-e5', (44, 25), ((44, 24.828), (44, 24.175), (44, 24)))
        self.add_bezier('sym-e6', (44, 24), ((44, 23.825), (44, 23.172), (44, 23)))
        self.add_bezier('sym-e7', (44, 23), ((44, 15.623), (37.473, 9.524), (30, 8)))
        self.add_bezier('sym-e8', (30, 8), ((28.982, 8), (28.036, 8), (27, 8)))
        self.add_line('sym-e9', (27, 8), (4, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
