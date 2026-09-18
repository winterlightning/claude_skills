"""Independent 32px profile of rounded-square-microchip-with-eight-pins.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '91baab07-2434-44bf-b597-92da30445815'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/safety helmet mine_91baab07-2434-44bf-b597-92da30445815.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('91baab07-2434-44bf-b597-92da30445815', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/safety helmet mine_91baab07-2434-44bf-b597-92da30445815.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rounded-square-microchip-with-eight-pins',)
SOLO_SOURCE_ICON_IDS = ('rounded-square-microchip-with-eight-pins',)
REFERENCE_EXPORT_SHA256 = '915ab20b05f26b0889089a862d5a9bbbdf3f451a453d3c44ecafce85a0ef26ff'

class Drawing(Sub32):
    icon_id = 'rounded-square-microchip-with-eight-pins-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/electronics'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 7), (13, 7))
        self.add_line('p1-r1-2', (13, 7), (19, 7))
        self.add_line('p1-r1-3', (19, 7), (22, 7))
        self.add_arc('p1-r1-4', (22, 7), (25, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (25, 10), (25, 13))
        self.add_line('p1-r1-6', (25, 13), (25, 19))
        self.add_line('p1-r1-7', (25, 19), (25, 22))
        self.add_arc('p1-r1-8', (25, 22), (22, 25), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (22, 25), (19, 25))
        self.add_line('p1-r1-10', (19, 25), (13, 25))
        self.add_line('p1-r1-11', (13, 25), (10, 25))
        self.add_arc('p1-r1-12', (10, 25), (7, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-13', (7, 22), (7, 19))
        self.add_line('p1-r1-14', (7, 19), (7, 13))
        self.add_line('p1-r1-15', (7, 13), (7, 10))
        self.add_arc('p1-r1-16', (7, 10), (10, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', closed=False)
        self.add_line('p2-r1-1', (13, 2), (13, 7))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (19, 2), (19, 7))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 13), (25, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (30, 19), (25, 19))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (19, 30), (19, 25))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (13, 30), (13, 25))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (2, 19), (7, 19))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (2, 13), (7, 13))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p4-r1-1')
        self.relate("connect", 'p1-r1-6', 'p4-r1-1')
        self.relate("connect", 'p1-r1-6', 'p5-r1-1')
        self.relate("connect", 'p1-r1-7', 'p5-r1-1')
        self.relate("connect", 'p1-r1-9', 'p6-r1-1')
        self.relate("connect", 'p1-r1-10', 'p6-r1-1')
        self.relate("connect", 'p1-r1-10', 'p7-r1-1')
        self.relate("connect", 'p1-r1-11', 'p7-r1-1')
        self.relate("connect", 'p1-r1-13', 'p8-r1-1')
        self.relate("connect", 'p1-r1-14', 'p8-r1-1')
        self.relate("connect", 'p1-r1-14', 'p9-r1-1')
        self.relate("connect", 'p1-r1-15', 'p9-r1-1')
