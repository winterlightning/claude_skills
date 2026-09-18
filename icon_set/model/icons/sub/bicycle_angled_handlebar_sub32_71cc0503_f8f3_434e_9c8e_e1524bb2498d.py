"""Independent 32px profile of bicycle-angled-handlebar.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '71cc0503-f8f3-434e-9c8e-e1524bb2498d'
SOURCE_PATH = 'pictographic-primitives/transportation/bicycle_71cc0503-f8f3-434e-9c8e-e1524bb2498d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('71cc0503-f8f3-434e-9c8e-e1524bb2498d', 'pictographic-primitives/transportation/bicycle_71cc0503-f8f3-434e-9c8e-e1524bb2498d.svg'), ('7e9c7c99-94c3-4ae5-a57d-56a00190f3e6', 'pictographic-primitives/transportation/bicycle_7e9c7c99-94c3-4ae5-a57d-56a00190f3e6.svg'))
PROFILE_SOURCE_KEYS = ('solo/bicycle-angled-handlebar',)
SOLO_SOURCE_ICON_IDS = ('bicycle-angled-handlebar',)
REFERENCE_EXPORT_SHA256 = '55370bf9c45f7da9d0c6c99aba8f5cf5e2577176e6f5cb8f78f4d6fba9eefe88'

class Drawing(Sub32):
    icon_id = 'bicycle-angled-handlebar-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 22), (12, 22), radius_x=5, radius_y=5, large_arc=True, sweep=False)
        self.add_arc('p1-r1-2', (12, 22), (2, 22), radius_x=5, radius_y=5, large_arc=True, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=True)
        self.add_arc('p2-r1-1', (20, 22), (30, 22), radius_x=5, radius_y=5, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 22), (20, 22), radius_x=5, radius_y=5, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=True)
        self.add_line('p3-r1-1', (7, 17), (13, 10))
        self.add_line('p3-r1-2', (13, 10), (20, 10))
        self.add_line('p3-r1-3', (20, 10), (25, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (5, 5), (10, 5))
        self.add_line('p4-r1-2', (10, 5), (13, 10))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (20, 10), (20, 7))
        self.add_line('p5-r1-2', (20, 7), (24, 5))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate("connect", 'p3-r1-1', 'p4-r1-2')
        self.relate("connect", 'p3-r1-2', 'p4-r1-2')
        self.relate("connect", 'p3-r1-2', 'p5-r1-1')
        self.relate("connect", 'p3-r1-3', 'p5-r1-1')
