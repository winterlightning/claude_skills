"""Independent 32px profile of state32-fc90d456-ac4f-4fc7-b86f-8210f32884cf.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'fc90d456-ac4f-4fc7-b86f-8210f32884cf'
SOURCE_PATH = 'icon_set/assets/combination-state32/fc90d456-ac4f-4fc7-b86f-8210f32884cf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fc90d456-ac4f-4fc7-b86f-8210f32884cf', 'icon_set/assets/combination-state32/fc90d456-ac4f-4fc7-b86f-8210f32884cf.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'b0b9915f9be16e9ef765fa327dd92c257eafe1a45fc1316695859ba21b74e78d'

class Drawing(Sub32):
    icon_id = 'state32-fc90d456-ac4f-4fc7-b86f-8210f32884cf'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (23, 2), ((27.666666666666664, 6.666666666666666), (30, 11.333333333333334), (30, 16)))
        self.add_line('p1-r1-2', (30, 16), (23, 16))
        self.add_line('p1-r1-3', (23, 16), (23, 30))
        self.add_line('p1-r1-4', (23, 30), (23, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (9, 17), (9, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (2, 10), (16, 10), radius_x=7, radius_y=7, large_arc=True, sweep=False)
        self.add_arc('p3-r1-2', (16, 10), (2, 10), radius_x=7, radius_y=7, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
