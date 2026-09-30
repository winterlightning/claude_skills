"""An empty web browser window: a rounded frame with a title bar across the top.

Symbol plan: rounded square frame; one full-width header rule split into the side walls.
Reduction: the reference's two small title-bar marks are dropped -- the 10-unit bar cannot hold
a mark with 8-unit clearance to both the top wall and the rule.
Keyshape: SQUARE.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c82821f8-144c-4e66-a040-a27f42442c4c'
SOURCE_PATH = 'pictographic-primitives/container/ui webpage template 1_c82821f8-144c-4e66-a040-a27f42442c4c.svg'
AUTHOR = 'claude-opus-5-5'

L, T, R, B, RAD, BAR = 6, 6, 42, 42, 5, 16


class Drawing(Solo48):
    icon_id = 'web-browser-window-blank'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives-generate')
    aliases = ('browser window', 'webpage template')
    keywords = ('browser', 'window', 'web', 'page', 'app')

    def build(self):
        self.add_line('frame-top', (L + RAD, T), (R - RAD, T))
        self.add_arc('frame-tr', (R - RAD, T), (R, T + RAD), radius_x=RAD)
        self.add_line('frame-right-a', (R, T + RAD), (R, BAR))
        self.add_line('frame-right-b', (R, BAR), (R, B - RAD))
        self.add_arc('frame-br', (R, B - RAD), (R - RAD, B), radius_x=RAD)
        self.add_line('frame-bottom', (R - RAD, B), (L + RAD, B))
        self.add_arc('frame-bl', (L + RAD, B), (L, B - RAD), radius_x=RAD)
        self.add_line('frame-left-b', (L, B - RAD), (L, BAR))
        self.add_line('frame-left-a', (L, BAR), (L, T + RAD))
        self.add_arc('frame-tl', (L, T + RAD), (L + RAD, T), radius_x=RAD)
        self.add_contour('frame', 'frame-top', 'frame-tr', 'frame-right-a', 'frame-right-b', 'frame-br',
                         'frame-bottom', 'frame-bl', 'frame-left-b', 'frame-left-a', 'frame-tl', closed=True)
        self.add_line('title-bar', (L, BAR), (R, BAR))
        self.relate('connect', 'title-bar', 'frame-left-a', 'frame-left-b')
        self.relate('connect', 'title-bar', 'frame-right-a', 'frame-right-b')
