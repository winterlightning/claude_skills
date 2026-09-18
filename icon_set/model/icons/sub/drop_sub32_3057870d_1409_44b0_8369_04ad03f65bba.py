"""Independent 32px profile of drop.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3057870d-1409-44b0-8369-04ad03f65bba'
SOURCE_PATH = 'pictographic-primitives/smileys/drop_3057870d-1409-44b0-8369-04ad03f65bba.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3057870d-1409-44b0-8369-04ad03f65bba', 'pictographic-primitives/smileys/drop_3057870d-1409-44b0-8369-04ad03f65bba.svg'), ('01d89380-da3f-4d8c-ae1a-a259c8c619ae', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/drop_01d89380-da3f-4d8c-ae1a-a259c8c619ae.svg'))
PROFILE_SOURCE_KEYS = ('solo/drop',)
SOLO_SOURCE_ICON_IDS = ('drop',)
REFERENCE_EXPORT_SHA256 = '57f5515bbc44864eb203afc87e7331eddc31dc8c2c7ce0087d67ddeecf7fe178'

class Drawing(Sub32):
    icon_id = 'drop-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'smileys'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((12, 7), (5, 15), (5, 19)))
        self.add_arc('p1-r1-2', (5, 19), (27, 19), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-3', (27, 19), ((27, 15), (20, 7), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
