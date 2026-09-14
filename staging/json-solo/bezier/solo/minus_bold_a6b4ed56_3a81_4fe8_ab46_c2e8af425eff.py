"""Minus bold (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6b4ed56-3a81-4fe8-ab46-c2e8af425eff'
SOURCE_PATH = 'icons-json/state/minus bold_a6b4ed56-3a81-4fe8-ab46-c2e8af425eff.json'
AUTHOR = 'json_to_solo'

class MinusBoldState(Solo48):
    icon_id = 'minus-bold-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('minus', 'bold', 'state')

    def build(self):
        self.add_line('sym-e0', (40, 40), (24, 40))
        self.add_line('sym-e1', (24, 40), (8, 40))
        self.add_bezier('sym-e2', (8, 40), ((6.364, 40), (4, 35.46), (4, 32)))
        self.add_bezier('sym-e3', (4, 32), ((4, 31.82), (4.009, 31.2), (4, 31)))
        self.add_bezier('sym-e4', (4, 31), ((4, 30.34), (4, 29.68), (4, 29)))
        self.add_bezier('sym-e5', (4, 29), ((4, 27.309), (4, 25.697), (4, 24)))
        self.add_bezier('sym-e6', (4, 24), ((4, 22.303), (4, 20.691), (4, 19)))
        self.add_bezier('sym-e7', (4, 19), ((4, 18.32), (4, 17.66), (4, 17)))
        self.add_bezier('sym-e8', (4, 17), ((4.009, 16.8), (4, 16.18), (4, 16)))
        self.add_bezier('sym-e9', (4, 16), ((4, 12.54), (6.364, 8), (8, 8)))
        self.add_line('sym-e10', (8, 8), (24, 8))
        self.add_line('sym-e11', (24, 8), (40, 8))
        self.add_bezier('sym-e12', (40, 8), ((41.636, 8), (44, 12.54), (44, 16)))
        self.add_bezier('sym-e13', (44, 16), ((44, 16.18), (43.991, 16.8), (44, 17)))
        self.add_bezier('sym-e14', (44, 17), ((44, 17.66), (44, 18.32), (44, 19)))
        self.add_bezier('sym-e15', (44, 19), ((44, 20.691), (44, 22.303), (44, 24)))
        self.add_bezier('sym-e16', (44, 24), ((44, 25.697), (44, 27.309), (44, 29)))
        self.add_bezier('sym-e17', (44, 29), ((44, 29.68), (44, 30.34), (44, 31)))
        self.add_bezier('sym-e18', (44, 31), ((43.991, 31.2), (44, 31.82), (44, 32)))
        self.add_bezier('sym-e19', (44, 32), ((44, 35.46), (41.636, 40), (40, 40)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
