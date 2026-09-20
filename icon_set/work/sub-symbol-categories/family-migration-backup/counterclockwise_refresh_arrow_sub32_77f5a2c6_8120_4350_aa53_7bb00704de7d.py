"""Independent 32px profile of counterclockwise-refresh-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '77f5a2c6-8120-4350-aa53-7bb00704de7d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/synchronize refresh arrow_77f5a2c6-8120-4350-aa53-7bb00704de7d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('77f5a2c6-8120-4350-aa53-7bb00704de7d', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/synchronize refresh arrow_77f5a2c6-8120-4350-aa53-7bb00704de7d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/counterclockwise-refresh-arrow',)
SOLO_SOURCE_ICON_IDS = ('counterclockwise-refresh-arrow',)
REFERENCE_EXPORT_SHA256 = '30d92cc2968ca337407f56ab814c76c75706859b73ce37125ae57732cb3f53e9'

class Drawing(Sub32):
    icon_id = 'counterclockwise-refresh-arrow-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 30), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 10), (2, 16))
        self.add_line('p2-r1-2', (2, 16), (8, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
