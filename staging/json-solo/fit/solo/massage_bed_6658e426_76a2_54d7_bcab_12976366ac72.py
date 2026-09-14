"""Massage bed (beauty), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6658e426-76a2-54d7-bcab-12976366ac72'
SOURCE_PATH = 'icons-json/beauty/massage bed_6658e426-76a2-54d7-bcab-12976366ac72.json'
AUTHOR = 'json_to_solo'

class MassageBedBeauty(Solo48):
    icon_id = 'massage-bed-beauty'
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
        self.add_line('sym-e4', (4, 16), (4, 15))
        self.add_line('sym-e6', (4, 15), (4, 13))
        self.add_line('sym-e9', (4, 13), (6, 8))
        self.add_arc('sym-e10', (6, 8), (7, 8), radius_x=7, sweep=False)
        self.add_line('sym-e11', (7, 8), (24, 8))
        self.add_line('sym-e12', (24, 8), (41, 8))
        self.add_line('sym-e13', (41, 8), (42, 8))
        self.add_line('sym-e14', (42, 8), (44, 13))
        self.add_line('sym-e17-1', (44, 13), (44, 14))
        self.add_arc('sym-e17-2', (44, 14), (44, 15), radius_x=24, sweep=False)
        self.add_line('sym-e19', (44, 15), (44, 16))
        self.add_line('sym-e20', (44, 16), (43, 18))
        self.add_line('sym-e21', (43, 18), (39, 18))
        self.add_line('sym-e22', (39, 18), (39, 29))
        self.add_line('sym-e23', (39, 29), (39, 40))
        self.add_line('sym-e24', (9, 29), (9, 40))
        self.add_line('sym-e25', (9, 18), (24, 18))
        self.add_line('sym-e26', (24, 18), (39, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e17-1', 'sym-e17-2', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.add_contour('sym-c1', 'sym-e24')
        self.add_contour('sym-c2', 'sym-e25', 'sym-e26')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
