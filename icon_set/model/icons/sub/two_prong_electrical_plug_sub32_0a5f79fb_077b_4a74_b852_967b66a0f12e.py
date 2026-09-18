"""Independent 32px profile of two-prong-electrical-plug.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0a5f79fb-077b-4a74-b852-967b66a0f12e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/plug_0a5f79fb-077b-4a74-b852-967b66a0f12e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0a5f79fb-077b-4a74-b852-967b66a0f12e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/plug_0a5f79fb-077b-4a74-b852-967b66a0f12e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/two-prong-electrical-plug',)
SOLO_SOURCE_ICON_IDS = ('two-prong-electrical-plug',)
REFERENCE_EXPORT_SHA256 = 'adbf25caff4acf5316d860bc89ebf43d1cfe8d54f54064296d0f68768e881e1a'

class Drawing(Sub32):
    icon_id = 'two-prong-electrical-plug-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 10), (10, 10))
        self.add_line('p1-r1-2', (10, 10), (22, 10))
        self.add_line('p1-r1-3', (22, 10), (27, 10))
        self.add_line('p1-r1-4', (27, 10), (27, 17))
        self.add_arc('p1-r1-5', (27, 17), (16, 24), radius_x=11, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (16, 24), (5, 17), radius_x=11, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (5, 17), (5, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (10, 2), (10, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 2), (22, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 24), (16, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p4-r1-1')
        self.relate("connect", 'p1-r1-6', 'p4-r1-1')
