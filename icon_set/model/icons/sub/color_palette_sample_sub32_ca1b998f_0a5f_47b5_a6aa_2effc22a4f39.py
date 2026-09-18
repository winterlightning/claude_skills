"""Independent 32px profile of color-palette-sample.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ca1b998f-0a5f-47b5-a6aa-2effc22a4f39'
SOURCE_PATH = 'pictographic-primitives/design/color palette sample_ca1b998f-0a5f-47b5-a6aa-2effc22a4f39.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ca1b998f-0a5f-47b5-a6aa-2effc22a4f39', 'pictographic-primitives/design/color palette sample_ca1b998f-0a5f-47b5-a6aa-2effc22a4f39.svg'),)
PROFILE_SOURCE_KEYS = ('solo/color-palette-sample',)
SOLO_SOURCE_ICON_IDS = ('color-palette-sample',)
REFERENCE_EXPORT_SHA256 = '014a3ec9066be4d14fb7a8b18f1004b9ffa2a5a8a4d81fd2dbc539e87faabac2'

class Drawing(Sub32):
    icon_id = 'color-palette-sample-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (17, 2), ((23, 2), (27, 6), (27, 11)))
        self.add_bezier('p1-r1-2', (27, 11), ((27, 16), (22, 17), (22, 22)))
        self.add_bezier('p1-r1-3', (22, 22), ((22, 26), (21, 30), (16, 30)))
        self.add_bezier('p1-r1-4', (16, 30), ((9, 30), (5, 24), (5, 17)))
        self.add_bezier('p1-r1-5', (5, 17), ((5, 10), (10, 2), (17, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (13, 14), (14, 15))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (19, 8), (19, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 22), (15, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
