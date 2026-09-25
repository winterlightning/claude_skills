"""Download Arrow: A vertical downward arrow points into a shallow U-shaped tray whose short ends curl upward. Generate this component alone; exclude Circle Frame.

Construction: A downward arrow is separated from a shallow tray with rounded lower corners.
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ce1e6086-e969-4822-a5e9-37e68d542f00'
SOURCE_PATH = 'pictographic-primitives/state/circle download_ce1e6086-e969-4822-a5e9-37e68d542f00.svg'
AUTHOR = 'gpt-6'


class DownloadArrowSub(Sub32):
    icon_id = 'download-arrow-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('download', 'arrow', 'vertical', 'downward', 'points', 'shallow', 'u', 'shaped')

    def build(self):
        self.add_line('shaft',(16,2),(16,20))
        self.add_polyline('head',(10,14),(16,20),(22,14))
        self.relate('connect','shaft','head')
        self.add_line('tray-left',(2,24),(2,27))
        self.add_arc('tray-lower-left',(2,27),(5,30),radius_x=3,sweep=False)
        self.add_line('tray-base',(5,30),(27,30))
        self.add_arc('tray-lower-right',(27,30),(30,27),radius_x=3,sweep=False)
        self.add_line('tray-right',(30,27),(30,24))
        self.add_contour('tray','tray-left','tray-lower-left','tray-base','tray-lower-right','tray-right')
