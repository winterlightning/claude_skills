"""Independent 32px profile of state32-22ebeb63-e3c2-4cdd-a779-46135c16e412.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '22ebeb63-e3c2-4cdd-a779-46135c16e412'
SOURCE_PATH = 'icon_set/assets/combination-state32/22ebeb63-e3c2-4cdd-a779-46135c16e412.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('22ebeb63-e3c2-4cdd-a779-46135c16e412', 'icon_set/assets/combination-state32/22ebeb63-e3c2-4cdd-a779-46135c16e412.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '77337268a8f32631866e8dc629356d18bace4e3d15876a0f4af9337e31c04651'

class Drawing(Sub32):
    icon_id = 'state32-22ebeb63-e3c2-4cdd-a779-46135c16e412'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 12), (24, 12))
        self.add_bezier('p1-r1-2', (24, 12), ((28, 12), (30, 10), (30, 7)))
        self.add_bezier('p1-r1-3', (30, 7), ((30, 5), (28, 2), (25, 2)))
        self.add_bezier('p1-r1-4', (25, 2), ((24, 2), (22, 2), (21, 3)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p1-r2-1', (2, 20), (18, 20))
        self.add_bezier('p1-r2-2', (18, 20), ((24, 20), (26, 23), (26, 26)))
        self.add_bezier('p1-r2-3', (26, 26), ((26, 28), (24, 30), (22, 30)))
        self.add_bezier('p1-r2-4', (22, 30), ((21, 30), (20, 30), (19, 29)))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', 'p1-r2-3', 'p1-r2-4', closed=False)
