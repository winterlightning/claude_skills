"""Independent 32px profile of ecology-leaf.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd816c758-0f95-4958-9d90-ed19c3a68e77'
SOURCE_PATH = 'pictographic-primitives/ecology/ecology leaf_d816c758-0f95-4958-9d90-ed19c3a68e77.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d816c758-0f95-4958-9d90-ed19c3a68e77', 'pictographic-primitives/ecology/ecology leaf_d816c758-0f95-4958-9d90-ed19c3a68e77.svg'), ('164d9e51-fa44-4293-94e6-d83af50f3387', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/leaf right_164d9e51-fa44-4293-94e6-d83af50f3387.svg'))
PROFILE_SOURCE_KEYS = ('solo/ecology-leaf',)
SOLO_SOURCE_ICON_IDS = ('ecology-leaf',)
REFERENCE_EXPORT_SHA256 = '3ed5069bfc0e588adb918c6a94a4e9604c79f6fe0df2f1a8f5693ff3058dbf1d'

class Drawing(Sub32):
    icon_id = 'ecology-leaf-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'ecology'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (30, 5), ((30, 16), (26, 24), (18, 26)))
        self.add_bezier('p1-r1-2', (18, 26), ((17, 27), (15, 27), (13, 27)))
        self.add_bezier('p1-r1-3', (13, 27), ((9, 27), (6, 26), (5, 23)))
        self.add_bezier('p1-r1-4', (5, 23), ((4, 22), (4, 20), (4, 19)))
        self.add_bezier('p1-r1-5', (4, 19), ((4, 13), (10, 8), (15, 8)))
        self.add_line('p1-r1-6', (15, 8), (22, 8))
        self.add_bezier('p1-r1-7', (22, 8), ((26, 8), (28, 6), (30, 5)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (2, 26), (5, 23))
        self.add_bezier('p2-r1-2', (5, 23), ((9, 19), (13, 16), (18, 14)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
