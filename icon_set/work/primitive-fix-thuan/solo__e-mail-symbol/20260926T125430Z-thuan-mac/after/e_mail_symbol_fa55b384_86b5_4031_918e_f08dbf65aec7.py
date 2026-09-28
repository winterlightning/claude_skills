"""e-mail symbol: a closed envelope seen from the front.
Review (meaning): the earlier deep U flap read as a bag. The reference and Lucide
`mail` both use a straight V flap from the two top corners, so this revision
restores that: a landscape rectangle with square centerline corners (round joins
still paint a soft corner) and a V whose apex sits at mid-height.
Keyshape HRECT_M (4,10)-(44,38): the reference envelope is about 3:2.
Lucide construction: mail (rect + V polyline from the top corners).
Omissions: none.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fa55b384-86b5-4031-918e-f08dbf65aec7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__e-mail-symbol/20260926T125430Z-thuan-mac/reference/e mail_fa55b384-86b5-4031-918e-f08dbf65aec7.svg'
AUTHOR = 'claude-opus-5-5'


class _Shapes:
    def circle(self, n, x, y, r):
        pts = [(x - r, y), (x, y - r), (x + r, y), (x, y + r), (x - r, y)]
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            self.add_arc(f"{n}-{i}", a, b, radius_x=r)
        self.add_contour(n, *(f"{n}-{i}" for i in range(4)), closed=True)

    def lines(self, n, *pts, closed=False):
        """Plain add_line segments grouped in one contour (members joinable by relate)."""
        seq = list(pts) + ([pts[0]] if closed else [])
        ids = []
        for i, (a, b) in enumerate(zip(seq, seq[1:])):
            self.add_line(f"{n}-{i}", a, b)
            ids.append(f"{n}-{i}")
        self.add_contour(n, *ids, closed=closed)
        return ids

class EMailSymbol(_Shapes, Solo48):
    icon_id = 'e-mail-symbol'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ('envelope', 'mail')
    keywords = ('e', 'mail', 'symbol', 'email', 'envelope', 'message', 'letter')

    def build(self):
        L, T, R, B = 4, 10, 44, 38
        apex = (24, 26)
        self.lines('envelope', (L, T), (R, T), (R, B), (L, B), closed=True)
        self.add_line('flap-l', (L, T), apex)
        self.add_line('flap-r', apex, (R, T))
        self.add_contour('flap', 'flap-l', 'flap-r')
        self.relate('connect', 'envelope', 'flap')
