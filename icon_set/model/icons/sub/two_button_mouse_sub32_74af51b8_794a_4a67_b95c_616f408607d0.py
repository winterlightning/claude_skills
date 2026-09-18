"""Independent 32px profile of two-button-mouse.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '74af51b8-794a-4a67-b95c-616f408607d0'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/mouse_74af51b8-794a-4a67-b95c-616f408607d0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('74af51b8-794a-4a67-b95c-616f408607d0', 'pictographic-primitives/computers/batch-03/mouse_74af51b8-794a-4a67-b95c-616f408607d0.svg'), ('dd2baaa6-8560-4803-ae47-3542cfdb8b76', 'pictographic-primitives/computers/batch-03/mouse_dd2baaa6-8560-4803-ae47-3542cfdb8b76.svg'))
PROFILE_SOURCE_KEYS = ('solo/two-button-mouse',)
SOLO_SOURCE_ICON_IDS = ('two-button-mouse',)
REFERENCE_EXPORT_SHA256 = '8e57f7ae41910079c91ec9c7f09868705317070d8afec6731494ae80db8a5244'

class Drawing(Sub32):
    icon_id = 'two-button-mouse-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/device'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (27, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (27, 13), (27, 15))
        self.add_line('p1-r1-3', (27, 15), (27, 19))
        self.add_arc('p1-r1-4', (27, 19), (16, 30), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (16, 30), (5, 19), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (5, 19), (5, 15))
        self.add_line('p1-r1-7', (5, 15), (5, 13))
        self.add_arc('p1-r1-8', (5, 13), (16, 2), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (5, 15), (16, 15))
        self.add_line('p2-r1-2', (16, 15), (27, 15))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
        self.relate("connect", 'p1-r1-8', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
