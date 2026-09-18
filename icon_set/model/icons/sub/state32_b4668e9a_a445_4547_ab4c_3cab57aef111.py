"""Independent 32px profile of state32-b4668e9a-a445-4547-ab4c-3cab57aef111.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b4668e9a-a445-4547-ab4c-3cab57aef111'
SOURCE_PATH = 'icon_set/assets/combination-state32/b4668e9a-a445-4547-ab4c-3cab57aef111.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b4668e9a-a445-4547-ab4c-3cab57aef111', 'icon_set/assets/combination-state32/b4668e9a-a445-4547-ab4c-3cab57aef111.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '9781087468c4a2b997be163c127c5244065f183fc8544bd99a069a313bc69deb'

class Drawing(Sub32):
    icon_id = 'state32-b4668e9a-a445-4547-ab4c-3cab57aef111'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_bezier('p1-r1-2', (24, 2), ((26, 2), (27, 3), (27, 5)))
        self.add_line('p1-r1-3', (27, 5), (27, 27))
        self.add_bezier('p1-r1-4', (27, 27), ((27, 29), (26, 30), (24, 30)))
        self.add_line('p1-r1-5', (24, 30), (8, 30))
        self.add_bezier('p1-r1-6', (8, 30), ((6, 30), (5, 29), (5, 27)))
        self.add_line('p1-r1-7', (5, 27), (5, 5))
        self.add_bezier('p1-r1-8', (5, 5), ((5, 3), (6, 2), (8, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (5, 24), (27, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (12, 9), (12, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, 9), (20, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
