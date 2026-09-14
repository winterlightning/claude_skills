"""Batch-02/astrology tail node (culture), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42841092-ec74-56d4-aedd-b98302173838'
SOURCE_PATH = 'icons-json/culture/batch-02/astrology tail node_42841092-ec74-56d4-aedd-b98302173838.json'
AUTHOR = 'json_to_solo'

class Batch02AstrologyTailNode(Solo48):
    icon_id = 'batch-02-astrology-tail-node'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'tail', 'node', 'culture')

    def build(self):
        self.add_line('sym-e0', (17, 16), (14, 30))
        self.add_arc('sym-e1', (14, 30), (23, 42), radius_x=11, sweep=False)
        self.add_line('sym-e2', (23, 42), (24, 42))
        self.add_line('sym-e5', (24, 42), (25, 42))
        self.add_arc('sym-e6', (25, 42), (34, 30), radius_x=11, sweep=False)
        self.add_line('sym-e7', (34, 30), (31, 16))
        self.add_arc('sym-e8', (31, 16), (32, 7), radius_x=8)
        self.add_line('sym-e9', (32, 7), (36, 6))
        self.add_arc('sym-e11', (36, 6), (42, 12), radius_x=6)
        self.add_arc('sym-e12', (42, 12), (42, 13), radius_x=23, sweep=False)
        self.add_arc('sym-e14', (42, 13), (41, 16), radius_x=6)
        self.add_arc('sym-e15', (41, 16), (34, 18), radius_x=6)
        self.add_arc('sym-e16', (34, 18), (32, 17), radius_x=9)
        self.add_line('sym-e17', (32, 17), (31, 16))
        self.add_line('sym-e19', (16, 17), (14, 18))
        self.add_arc('sym-e20', (14, 18), (7, 16), radius_x=6)
        self.add_arc('sym-e21', (7, 16), (6, 13), radius_x=6)
        self.add_line('sym-e23', (6, 13), (6, 12))
        self.add_arc('sym-e24', (6, 12), (12, 6), radius_x=6)
        self.add_line('sym-e26', (12, 6), (16, 7))
        self.add_arc('sym-e27', (16, 7), (17, 16), radius_x=7)
        self.add_line('sym-e29', (17, 16), (16, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17')
        self.add_contour('sym-c1', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24', 'sym-e26', 'sym-e27', 'sym-e29', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
