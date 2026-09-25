"""Independent 32px profile of coffee-cup-steam.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a305ae9d-2a1c-4b82-b834-da8cd3ba1072'
SOURCE_PATH = 'pictographic-primitives/symbol/coffee_a305ae9d-2a1c-4b82-b834-da8cd3ba1072.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a305ae9d-2a1c-4b82-b834-da8cd3ba1072', 'pictographic-primitives/symbol/coffee_a305ae9d-2a1c-4b82-b834-da8cd3ba1072.svg'),)
PROFILE_SOURCE_KEYS = ('solo/coffee-cup-steam',)
SOLO_SOURCE_ICON_IDS = ('coffee-cup-steam',)
REFERENCE_EXPORT_SHA256 = 'bc7d9eebce204a4f7239b6aee85ba21cbe13059b73ff6252735a40a5c0ec11e1'

class Drawing(Sub32):
    icon_id = 'coffee-cup-steam-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 15), (21, 15))
        self.add_line('p1-r1-2', (21, 15), (21, 16))
        self.add_line('p1-r1-3', (21, 16), (21, 24))
        self.add_bezier('p1-r1-4', (21, 24), ((21, 25), (20, 27), (19, 28)))
        self.add_bezier('p1-r1-5', (19, 28), ((18, 29), (16, 30), (14, 30)))
        self.add_line('p1-r1-6', (14, 30), (8, 30))
        self.add_arc('p1-r1-7', (8, 30), (2, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (2, 24), (2, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (21, 16), (25, 16))
        self.add_arc('p2-r1-2', (25, 16), (30, 20), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (30, 20), (25, 24), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (25, 24), (21, 24))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_arc('p3-r1-1', (7, 2), (7, 5), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p3-r1-2', (7, 5), (7, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (16, 2), (16, 5), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p4-r1-2', (16, 5), (16, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-4')
        self.relate("connect", 'p1-r1-4', 'p2-r1-4')
