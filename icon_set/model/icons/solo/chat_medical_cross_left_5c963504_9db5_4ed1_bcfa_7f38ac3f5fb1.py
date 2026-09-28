"""Square speech panel with lower-left tail and a big outlined medical cross.
Revision (review: "cross_big"): the cross now fills the bubble interior, 16 x 16
(arms 8 wide, reaching 8 from the centre (24,22); was 14 x 14), exactly 8 from the top wall
and the bottom edge: the largest cross the bubble interior allows.
Construction: Tail direction and outlined cross retained; bubble corners are square
on the centerline (rounded by the round joins) so the exact 8 certifies.
Lucide construction reference: message-circle-plus; coherent arcs and independent enclosed content.
Keyshape SQUARE: (4,4)-(44,44) ink.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c963504-9db5-4ed1-bcfa-7f38ac3f5fb1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chat-medical-cross-left/20260926T125429Z-thuan-mac/reference/chat medical cross left_5c963504-9db5-4ed1-bcfa-7f38ac3f5fb1.svg'
AUTHOR = 'claude-opus-5-5'

class Drawing(Solo48):
    icon_id = 'chat-medical-cross-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('chat', 'medical', 'cross', 'left')

    def build(self):
        # Rounded speech enclosure, lower-left tail, and outlined medical cross.
        # square centerline corners: the round joins paint them with an ink
        # radius of 2, and every wall-to-cross distance stays straight-to-straight
        pts = [(6,6),(42,6),(42,38),(18,38),(14,42),(14,38),(6,38)]
        self.add_polyline('bubble', *pts, closed=True)
        cx, cy, outer, stem = 24, 22, 8, 4
        pts = [(-stem,-outer),(stem,-outer),(stem,-stem),(outer,-stem),(outer,stem),(stem,stem),(stem,outer),(-stem,outer),(-stem,stem),(-outer,stem),(-outer,-stem),(-stem,-stem)]
        self.add_polyline('medical-cross', *((cx+x,cy+y) for x,y in pts), closed=True)

