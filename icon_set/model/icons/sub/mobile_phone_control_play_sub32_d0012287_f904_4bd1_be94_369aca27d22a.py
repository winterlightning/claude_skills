"""Independent 32px profile of mobile-phone-control-play.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd0012287-f904-4bd1-be94-369aca27d22a'
SOURCE_PATH = 'pictographic-primitives/state/mobile phone control play_d0012287-f904-4bd1-be94-369aca27d22a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d0012287-f904-4bd1-be94-369aca27d22a', 'pictographic-primitives/state/mobile phone control play_d0012287-f904-4bd1-be94-369aca27d22a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mobile-phone-control-play',)
SOLO_SOURCE_ICON_IDS = ('mobile-phone-control-play',)
REFERENCE_EXPORT_SHA256 = '8a6e70040bac9b1e07cb53acbab666753626bb3bb9e43c2bcd30a94088ff1387'

class Drawing(Sub32):
    icon_id = 'mobile-phone-control-play-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_arc('p1-r1-2', (24, 2), (27, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 5), (27, 24))
        self.add_line('p1-r1-4', (27, 24), (27, 27))
        self.add_arc('p1-r1-5', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (24, 30), (8, 30))
        self.add_arc('p1-r1-7', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (5, 27), (5, 24))
        self.add_line('p1-r1-9', (5, 24), (5, 5))
        self.add_arc('p1-r1-10', (5, 5), (8, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (5, 24), (27, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (12, 8), (20, 13))
        self.add_line('p3-r1-2', (20, 13), (12, 17))
        self.add_line('p3-r1-3', (12, 17), (12, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
