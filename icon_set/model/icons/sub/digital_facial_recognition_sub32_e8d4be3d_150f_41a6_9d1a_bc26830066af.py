"""Independent 32px profile of digital-facial-recognition.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e8d4be3d-150f-41a6-9d1a-bc26830066af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/deepfake_e8d4be3d-150f-41a6-9d1a-bc26830066af.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e8d4be3d-150f-41a6-9d1a-bc26830066af', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/deepfake_e8d4be3d-150f-41a6-9d1a-bc26830066af.svg'),)
PROFILE_SOURCE_KEYS = ('solo/digital-facial-recognition',)
SOLO_SOURCE_ICON_IDS = ('digital-facial-recognition',)
REFERENCE_EXPORT_SHA256 = 'e827b403f0f2d98ad6e17a3c029a6b96aa2d7c5f71feae73879022078538d516'

class Drawing(Sub32):
    icon_id = 'digital-facial-recognition-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 13), (27, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (27, 13), (27, 19))
        self.add_arc('p1-r1-3', (27, 19), (5, 19), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (5, 19), (5, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (5, 13), (27, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (13, 22), ((14, 23), (15, 23), (16, 23)))
        self.add_bezier('p4-r1-2', (16, 23), ((17, 23), (18, 23), (20, 22)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
