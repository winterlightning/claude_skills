"""Independent 32px profile of factory-with-twin-chimneys-153adb1d.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '153adb1d-99b9-4795-8617-0258a4f8d507'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/factory_153adb1d-99b9-4795-8617-0258a4f8d507.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('153adb1d-99b9-4795-8617-0258a4f8d507', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/factory_153adb1d-99b9-4795-8617-0258a4f8d507.svg'), ('2530cf14-a84f-4082-8504-b4d2f35fe972', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/factory_2530cf14-a84f-4082-8504-b4d2f35fe972.svg'))
PROFILE_SOURCE_KEYS = ('solo/factory-with-twin-chimneys-153adb1d',)
SOLO_SOURCE_ICON_IDS = ('factory-with-twin-chimneys-153adb1d',)
REFERENCE_EXPORT_SHA256 = '4d38d41e19b5ed38fa682b84a4a6dbc0d0cc1ec38dfb6a13e74154af1199b455'

class Drawing(Sub32):
    icon_id = 'factory-with-twin-chimneys-153adb1d-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/factory'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 18), (10, 18))
        self.add_line('p1-r1-2', (10, 18), (16, 13))
        self.add_line('p1-r1-3', (16, 13), (22, 18))
        self.add_line('p1-r1-4', (22, 18), (30, 18))
        self.add_line('p1-r1-5', (30, 18), (30, 30))
        self.add_line('p1-r1-6', (30, 30), (2, 30))
        self.add_line('p1-r1-7', (2, 30), (2, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (2, 18), (2, 2))
        self.add_line('p2-r1-2', (2, 2), (8, 2))
        self.add_line('p2-r1-3', (8, 2), (10, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (30, 18), (30, 2))
        self.add_line('p3-r1-2', (30, 2), (24, 2))
        self.add_line('p3-r1-3', (24, 2), (22, 18))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-3')
        self.relate("connect", 'p1-r1-2', 'p2-r1-3')
        self.relate("connect", 'p1-r1-3', 'p3-r1-3')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-3')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
