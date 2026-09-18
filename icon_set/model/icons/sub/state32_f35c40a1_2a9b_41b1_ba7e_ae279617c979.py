"""Independent 32px profile of state32-f35c40a1-2a9b-41b1-ba7e-ae279617c979.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f35c40a1-2a9b-41b1-ba7e-ae279617c979'
SOURCE_PATH = 'icon_set/assets/combination-state32/f35c40a1-2a9b-41b1-ba7e-ae279617c979.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f35c40a1-2a9b-41b1-ba7e-ae279617c979', 'icon_set/assets/combination-state32/f35c40a1-2a9b-41b1-ba7e-ae279617c979.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'c4956554b68dcd025fa02cff256ac435f136a76d72a5620fea3e254a7f9f99d3'

class Drawing(Sub32):
    icon_id = 'state32-f35c40a1-2a9b-41b1-ba7e-ae279617c979'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 20), (20, 12))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p1-r2-1', (14, 12), (20, 12))
        self.add_line('p1-r2-2', (20, 12), (20, 18))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p1-r2-1')
        self.relate("connect", 'p1-r1-1', 'p1-r2-2')
