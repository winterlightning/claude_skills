"""Rotation y axis (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7bd2a8a-4fad-494e-95b4-c6de9862f81d'
SOURCE_PATH = 'icons-json/design/rotation y axis_e7bd2a8a-4fad-494e-95b4-c6de9862f81d.json'
AUTHOR = 'json_to_solo'

class RotationYAxisDesign(Solo48):
    icon_id = 'rotation-y-axis-design'
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
        self.add_bezier('e5', (15, 17), ((11.915, 18.072), (6.008, 19.934), (6.008, 23.943)), ((6.008, 23.975), (6, 24.007), (6, 24.039)), ((6, 24.04), (6, 24.04), (6, 24.041)), ((6, 24.188), (6.008, 24.327), (6.008, 24.475)), ((6.008, 26.569), (8.127, 28.156), (9.715, 29.146)), ((13.945, 31.789), (18.214, 31.681), (23, 32)))
        self.add_bezier('e6', (34, 16), ((36.79, 17.432), (41.992, 19.68), (41.992, 23.542)), ((41.992, 23.615), (42, 23.681), (42, 23.755)), ((42, 23.756), (42, 23.757), (42, 23.758)), ((42, 23.83), (42, 23.895), (42, 23.967)), ((42, 26.373), (39.734, 28.214), (37.86, 29.318)), ((33.229, 32.043), (28.212, 32.008), (23, 32)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e4')
        self.add_contour('c5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
