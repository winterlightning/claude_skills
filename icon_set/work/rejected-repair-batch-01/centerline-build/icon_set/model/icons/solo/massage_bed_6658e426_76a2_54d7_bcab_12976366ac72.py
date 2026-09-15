"""Massage bed (beauty), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6658e426-76a2-54d7-bcab-12976366ac72'
SOURCE_PATH = 'pictographic-primitives/beauty/massage bed_6658e426-76a2-54d7-bcab-12976366ac72.svg'
AUTHOR = 'gpt-6'

class MassageBed(Solo48):
    icon_id = 'massage-bed'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('massage', 'bed', 'beauty')

    def build(self):
        self.add_line('sym-e0', (39, 29), (9, 29))
        self.add_line('sym-e1', (9, 29), (9, 18))
        self.add_line('sym-e2', (9, 18), (5, 18))
        self.add_line('sym-e3', (5, 18), (4, 16))
        self.add_line('sym-e4', (4, 16), (4, 13))
        self.add_line('sym-e9', (4, 13), (6, 8))
        self.add_arc('sym-e10', (6, 8), (7, 8), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e11', (7, 8), (42, 8))
        self.add_line('sym-e14', (42, 8), (44, 13))
        self.add_line('sym-e17-1', (44, 13), (44, 14))
        self.add_arc('sym-e17-2', (44, 14), (44, 15), radius_x=24, radius_y=24, large_arc=False, sweep=False)
        self.add_line('sym-e19', (44, 15), (44, 16))
        self.add_line('sym-e20', (44, 16), (43, 18))
        self.add_line('sym-e21', (43, 18), (39, 18))
        self.add_line('sym-e22', (39, 18), (39, 40))
        self.add_line('sym-e24', (9, 29), (9, 40))
        self.add_line('sym-e25', (9, 18), (39, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e14', 'sym-e17-1', 'sym-e17-2', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', closed=False)
        self.add_contour('sym-c1', 'sym-e24', closed=False)
        self.add_contour('sym-c2', 'sym-e25', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
