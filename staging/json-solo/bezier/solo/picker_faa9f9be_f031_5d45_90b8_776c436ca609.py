"""Picker (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'faa9f9be-f031-5d45-90b8-776c436ca609'
SOURCE_PATH = 'icons-json/design/picker_faa9f9be-f031-5d45-90b8-776c436ca609.json'
AUTHOR = 'json_to_solo'

class PickerFaa9f9be(Solo48):
    icon_id = 'picker-faa9f9be'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('picker', 'design')

    def build(self):
        self.add_line('sym-e0', (40, 18), (8, 18))
        self.add_bezier('sym-e1', (14, 10), ((14, 6.482), (15.848, 4), (23, 4)))
        self.add_bezier('sym-e2', (23, 4), ((23.186, 4), (23.813, 4), (24, 4)))
        self.add_bezier('sym-e3', (24, 4), ((24.187, 4), (24.814, 4), (25, 4)))
        self.add_bezier('sym-e4', (25, 4), ((32.152, 4), (34, 6.482), (34, 10)))
        self.add_line('sym-e5', (34, 10), (34, 31))
        self.add_bezier('sym-e6', (34, 31), ((34, 31.312), (34, 31.665), (34, 32)))
        self.add_bezier('sym-e7', (34, 32), ((34, 32.954), (33.675, 34.172), (33, 35)))
        self.add_bezier('sym-e8', (33, 35), ((32.008, 36.218), (29.448, 37.655), (29, 39)))
        self.add_bezier('sym-e9', (29, 39), ((28.456, 40.655), (30.8, 44), (26, 44)))
        self.add_bezier('sym-e10', (26, 44), ((25.387, 44), (24.613, 44), (24, 44)))
        self.add_bezier('sym-e11', (24, 44), ((23.387, 44), (22.613, 44), (22, 44)))
        self.add_bezier('sym-e12', (22, 44), ((17.2, 44), (19.544, 40.655), (19, 39)))
        self.add_bezier('sym-e13', (19, 39), ((18.552, 37.655), (15.992, 36.218), (15, 35)))
        self.add_bezier('sym-e14', (15, 35), ((14.325, 34.172), (14, 32.954), (14, 32)))
        self.add_bezier('sym-e15', (14, 32), ((14, 31.665), (14, 31.312), (14, 31)))
        self.add_line('sym-e16', (14, 31), (14, 10))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
