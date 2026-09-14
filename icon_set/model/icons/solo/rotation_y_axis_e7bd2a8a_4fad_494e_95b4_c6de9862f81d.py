"""Rotation y axis (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7bd2a8a-4fad-494e-95b4-c6de9862f81d'
SOURCE_PATH = 'icons-json/design/rotation y axis_e7bd2a8a-4fad-494e-95b4-c6de9862f81d.json'
AUTHOR = 'json_to_solo'

class RotationYAxis(Solo48):
    icon_id = 'rotation-y-axis'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rotation', 'y', 'axis', 'design')

    def build(self):
        self.add_line('e0', (23, 6), (23, 32))
        self.add_line('e1', (23, 42), (23, 32))
        self.add_line('e2', (40, 15), (34, 16))
        self.add_line('e3', (35, 22), (35, 18))
        self.add_line('e4', (35, 18), (34, 16))
        self.add_arc('e5-1', (15, 17), (6, 24), radius_x=10, sweep=False)
        self.add_arc('e5-2', (6, 24), (11, 30), radius_x=7, sweep=False)
        self.add_arc('e5-3', (11, 30), (23, 32), radius_x=29, sweep=False)
        self.add_arc('e6-1', (34, 16), (42, 24), radius_x=10)
        self.add_arc('e6-2', (42, 24), (34, 31), radius_x=9)
        self.add_arc('e6-3', (34, 31), (23, 32), radius_x=34)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e4')
        self.add_contour('c5', 'e6-1', 'e6-2', 'e6-3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
