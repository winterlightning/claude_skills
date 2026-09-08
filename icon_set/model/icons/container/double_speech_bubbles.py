"""Two overlapping rectangular speech bubbles have opposing lower tails.

Keyshape SQUARE: visible bounds (0, 0, 64, 64).
Lucide messages-square informs rounded rectangles, tails and an interrupted rear
outline. Source layout retains a dominant upper-left bubble and smaller lower-right
reply. Centerline extremes (2,2)-(62,62). Directional overlap is intentional;
small export irregularities are removed.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class DoubleSpeechBubbles(Container64):
    icon_id = 'double-speech-bubbles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('conversation-bubbles',)
    keywords = ('chat', 'dialogue', 'speech', 'messages')

    def build(self) -> None:
        self.add_line('front-top', (6, 2), (46, 2))
        self.add_arc('front-ne', (46, 2), (50, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_line('front-right', (50, 6), (50, 36))
        self.add_arc('front-se', (50, 36), (46, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('front-bottom', (46, 40), (22, 40))
        self.add_line('tail-diagonal', (22, 40), (10, 50))
        self.add_line('tail-vertical', (10, 50), (10, 40))
        self.add_line('front-bottom-left', (10, 40), (6, 40))
        self.add_arc('front-sw', (6, 40), (2, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('front-left', (2, 36), (2, 6))
        self.add_arc('front-nw', (2, 6), (6, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('front', 'front-top', 'front-ne', 'front-right', 'front-se', 'front-bottom', 'tail-diagonal', 'tail-vertical', 'front-bottom-left', 'front-sw', 'front-left', 'front-nw', closed=True)
        self.add_line('rear-top', (50, 30), (58, 30))
        self.add_arc('rear-ne', (58, 30), (62, 34), radius_x=4, radius_y=4, sweep=True)
        self.add_line('rear-right', (62, 34), (62, 52))
        self.add_line('rear-notch', (62, 52), (58, 52))
        self.add_line('rear-tail-right', (58, 52), (58, 62))
        self.add_line('rear-tail-diagonal', (58, 62), (44, 52))
        self.add_line('rear-bottom', (44, 52), (34, 52))
        self.add_arc('rear-sw', (34, 52), (30, 48), radius_x=4, radius_y=4, sweep=True)
        self.add_line('rear-left', (30, 48), (30, 40))
        self.add_contour('rear', 'rear-top', 'rear-ne', 'rear-right', 'rear-notch', 'rear-tail-right', 'rear-tail-diagonal', 'rear-bottom', 'rear-sw', 'rear-left', closed=False)
        self.relate("connect", 'front', 'rear')
