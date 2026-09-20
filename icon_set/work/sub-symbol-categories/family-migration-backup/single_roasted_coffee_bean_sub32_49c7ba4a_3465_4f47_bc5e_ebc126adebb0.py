"""Independent 32px profile of single-roasted-coffee-bean.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '49c7ba4a-3465-4f47-bc5e-ebc126adebb0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/coffee bean_49c7ba4a-3465-4f47-bc5e-ebc126adebb0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('49c7ba4a-3465-4f47-bc5e-ebc126adebb0', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/coffee bean_49c7ba4a-3465-4f47-bc5e-ebc126adebb0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/single-roasted-coffee-bean',)
SOLO_SOURCE_ICON_IDS = ('single-roasted-coffee-bean',)
REFERENCE_EXPORT_SHA256 = 'c2c9cea1d494d0f4759f19b81059f3a4b085868ba7dc19d337b594eec0c18c0e'

class Drawing(Sub32):
    icon_id = 'single-roasted-coffee-bean-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 16), (16, 2), radius_x=11, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (27, 16), radius_x=11, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (27, 16), (16, 30), radius_x=11, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 30), (5, 16), radius_x=11, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (16, 2), ((18, 4), (18, 6), (18, 8)))
        self.add_bezier('p2-r1-2', (18, 8), ((18, 13), (14, 19), (14, 24)))
        self.add_bezier('p2-r1-3', (14, 24), ((14, 26), (14, 28), (16, 30)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')
        self.relate("connect", 'p1-r1-4', 'p2-r1-3')
