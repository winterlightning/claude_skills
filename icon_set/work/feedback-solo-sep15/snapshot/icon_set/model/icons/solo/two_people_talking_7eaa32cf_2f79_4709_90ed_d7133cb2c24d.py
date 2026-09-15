"""Two overlapping busts sit below a large speech bubble at the upper left. Curved hairlines cross both heads, and the bubble has a short downward tail and two horizontal text lines.
Lucide message-square rounded corners and users head/shoulder construction. Two overlapping participants retain the source arrangement. Bubble text, hairlines and chest mark omitted for clear space. Deliberate rear-left/front-right asymmetry.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7eaa32cf-2f79-4709-90ed-d7133cb2c24d'
SOURCE_PATH = 'pictographic-primitives/work/team meeting chat_7eaa32cf-2f79-4709-90ed-d7133cb2c24d.svg'
AUTHOR = 'gpt-6'


class TwoPeopleTalking(Solo48):
    icon_id = 'two-people-talking'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('people', 'conversation', 'meeting', 'speech', 'chat', 'team')

    def build(self) -> None:
        self.add_line('bubble-top', (10, 6), (22, 6))
        self.add_arc('corner-ne', (22, 6), (26, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bubble-right', (26, 10), (26, 14))
        self.add_arc('corner-se', (26, 14), (22, 18), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_polyline('tail', (22, 18), (20, 22), (14, 18), (10, 18), closed=False)
        self.add_arc('corner-sw', (10, 18), (6, 14), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bubble-left', (6, 14), (6, 10))
        self.add_arc('corner-nw', (6, 10), (10, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('bubble', 'bubble-top', 'corner-ne', 'bubble-right', 'corner-se', closed=False)
        self.relate("connect", 'bubble', 'tail')
        self.relate("connect", 'tail', 'corner-sw')
        self.relate("connect", 'corner-sw', 'bubble-left')
        self.relate("connect", 'bubble-left', 'corner-nw')
        self.relate("connect", 'corner-nw', 'bubble')
        self.add_arc('front-head-top', (30, 27), (38, 27), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('front-head-bottom', (38, 27), (30, 27), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('front-head', 'front-head-top', 'front-head-bottom', closed=True)
        self.add_arc('front-left', (26, 42), (34, 40), radius_x=8, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('front-right', (34, 40), (42, 42), radius_x=8, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('front-bust', 'front-left', 'front-right', closed=False)
        self.add_arc('rear-head-top', (11, 33), (17, 33), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('rear-head-bottom', (17, 33), (11, 33), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('rear-head', 'rear-head-top', 'rear-head-bottom', closed=True)
        self.add_arc('rear-left', (6, 42), (14, 36), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('rear-right', (14, 36), (26, 42), radius_x=12, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('rear-bust', 'rear-left', 'rear-right', closed=False)
        self.relate("connect", 'rear-head', 'rear-bust')
        self.relate("connect", 'rear-bust', 'front-bust')
