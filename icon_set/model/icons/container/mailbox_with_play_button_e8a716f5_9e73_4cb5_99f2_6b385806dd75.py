"""Banded vertical media frame with its central play triangle.

Preserve the whole subject per the authoritative TODO decision. The source
reads as a media frame, not a physical mailbox. VRECT_XL (6,2)-(58,62)
supports a tall shell, paired rails and top/bottom bands. Lucide
panels-top-left informs shared divider nodes and rounded perimeter turns.
All frame geometry mirrors about x=32; the play triangle points right.
Complete the clipped lower shell; omit no semantic component.
Hosting via compose.py: check-mark validates; plus-sign-state-131 is invalid
for parallel spacing against play; heart-state-63 returns review for rail
contact. Legacy probe IDs plus/heart/check are absent from this registry.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path

SOURCE_ICON_ID = 'e8a716f5-9e73-4cb5-99f2-6b385806dd75'
SOURCE_PATH = 'pictographic-primitives/emails/mailbox post_e8a716f5-9e73-4cb5-99f2-6b385806dd75.svg'
AUTHOR = 'gpt-6'

class Drawing(Container64):
    icon_id = 'mailbox-with-play-button'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ('banded vertical media frame',)
    keywords = ('mailbox','with','play','button')

    def build(self):
        axis, rail_left = 32, 18
        rail_right = 2*axis-rail_left
        path(self,'shell',(16,2),[
            ('L',(rail_left,2)),('L',(rail_right,2)),('L',(48,2)),
            ('A',(58,12),10,10,True),('L',(58,52)),
            ('A',(48,62),10,10,True),('L',(rail_right,62)),
            ('L',(rail_left,62)),('L',(16,62)),
            ('A',(6,52),10,10,True),('L',(6,12)),
            ('A',(16,2),10,10,True)],closed=True)
        for side,x in [('left',rail_left),('right',rail_right)]:
            self.add_polyline(side+'-rail',(x,2),(x,16),(x,52),(x,62))
            self.relate('connect','shell',side+'-rail')
        for name,y in [('top-band',16),('bottom-band',52)]:
            self.add_line(name,(rail_left,y),(rail_right,y))
            for side in ('left','right'):
                self.relate('connect',name,side+'-rail')
        self.add_polyline('play',(26,26),(38,34),(26,42),closed=True)
