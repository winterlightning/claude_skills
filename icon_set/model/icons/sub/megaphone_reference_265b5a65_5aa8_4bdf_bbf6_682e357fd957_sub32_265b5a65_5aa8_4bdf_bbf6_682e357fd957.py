"""Independent 32px profile of megaphone-reference-265b5a65-5aa8-4bdf-bbf6-682e357fd957.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '265b5a65-5aa8-4bdf-bbf6-682e357fd957'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/megaphone_265b5a65-5aa8-4bdf-bbf6-682e357fd957.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('265b5a65-5aa8-4bdf-bbf6-682e357fd957', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/megaphone_265b5a65-5aa8-4bdf-bbf6-682e357fd957.svg'), ('3eda77ef-4a51-4c20-a561-a20d8a86f04f', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/megaphone_3eda77ef-4a51-4c20-a561-a20d8a86f04f.svg'))
PROFILE_SOURCE_KEYS = ('solo/megaphone-reference-265b5a65-5aa8-4bdf-bbf6-682e357fd957', 'solo/megaphone-reference-3eda77ef-4a51-4c20-a561-a20d8a86f04f')
SOLO_SOURCE_ICON_IDS = ('megaphone-reference-265b5a65-5aa8-4bdf-bbf6-682e357fd957', 'megaphone-reference-3eda77ef-4a51-4c20-a561-a20d8a86f04f')
REFERENCE_EXPORT_SHA256 = 'd1525e9cc1fe02587ff1eb4a79d5fb47336a3e39be578ecc4d3a719d4d5fba54'

class Drawing(Sub32):
    icon_id = 'megaphone-reference-265b5a65-5aa8-4bdf-bbf6-682e357fd957-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 18), (21, 2))
        self.add_line('p1-r1-2', (21, 2), (30, 18))
        self.add_line('p1-r1-3', (30, 18), (21, 19))
        self.add_line('p1-r1-4', (21, 19), (11, 21))
        self.add_line('p1-r1-5', (11, 21), (5, 22))
        self.add_line('p1-r1-6', (5, 22), (2, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_bezier('p2-r1-1', (11, 21), ((11, 27), (13, 30), (16, 30)))
        self.add_bezier('p2-r1-2', (16, 30), ((19, 30), (21, 27), (21, 19)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
