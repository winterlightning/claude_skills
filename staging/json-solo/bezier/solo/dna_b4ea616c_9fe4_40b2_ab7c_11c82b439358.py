"""Dna (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4ea616c-9fe4-40b2-ab7c-11c82b439358'
SOURCE_PATH = 'icons-json/artificial-intelligence/dna_b4ea616c-9fe4-40b2-ab7c-11c82b439358.json'
AUTHOR = 'json_to_solo'

class DnaB4ea616c(Solo48):
    icon_id = 'dna-b4ea616c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('dna', 'artificial-intelligence')

    def build(self):
        self.add_line('sym-e0', (8, 40), (40, 40))
        self.add_bezier('sym-e1', (40, 40), ((40, 39.073), (39.42, 37.855), (39, 37)))
        self.add_bezier('sym-e2', (39, 37), ((37.65, 34.236), (35.22, 31.218), (33, 29)))
        self.add_bezier('sym-e3', (33, 29), ((32.04, 28.045), (31.19, 27.718), (30, 27)))
        self.add_line('sym-e4', (30, 27), (24, 23))
        self.add_line('sym-e5', (24, 23), (25, 22))
        self.add_bezier('sym-e6', (25, 22), ((26.18, 21.109), (27.75, 20.809), (29, 20)))
        self.add_bezier('sym-e7', (29, 20), ((33.87, 16.873), (37.27, 14.3), (39, 9)))
        self.add_line('sym-e8', (39, 9), (9, 9))
        self.add_bezier('sym-e9', (9, 9), ((10.73, 14.3), (14.13, 16.873), (19, 20)))
        self.add_bezier('sym-e10', (19, 20), ((20.25, 20.809), (21.82, 21.109), (23, 22)))
        self.add_line('sym-e11', (23, 22), (24, 23))
        self.add_line('sym-e12', (24, 23), (18, 27))
        self.add_bezier('sym-e13', (18, 27), ((16.81, 27.718), (15.96, 28.045), (15, 29)))
        self.add_bezier('sym-e14', (15, 29), ((12.78, 31.218), (10.35, 34.236), (9, 37)))
        self.add_bezier('sym-e15', (9, 37), ((8.58, 37.855), (8, 39.073), (8, 40)))
        self.add_bezier('sym-e16', (8, 40), ((8, 41.209), (8, 42.791), (8, 44)))
        self.add_bezier('sym-e17', (40, 40), ((40, 41.209), (40, 42.791), (40, 44)))
        self.add_bezier('sym-e18', (39, 9), ((39.45, 7.618), (40, 5.445), (40, 4)))
        self.add_bezier('sym-e19', (40, 4), ((40, 4), (40, 4.027), (40, 4)))
        self.add_bezier('sym-e20', (40, 4), ((40, 4), (40, 4.018), (40, 4)))
        self.add_bezier('sym-e21', (9, 9), ((8.55, 7.618), (8, 5.445), (8, 4)))
        self.add_bezier('sym-e22', (8, 4), ((8, 4), (8, 4.027), (8, 4)))
        self.add_bezier('sym-e23', (8, 4), ((8, 4), (8, 4.018), (8, 4)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c1', 'sym-e17')
        self.add_contour('sym-c2', 'sym-e18', 'sym-e19', 'sym-e20')
        self.add_contour('sym-c3', 'sym-e21', 'sym-e22', 'sym-e23')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
