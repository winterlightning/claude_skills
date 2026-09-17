"""Chinese Endless Knot.

Plan: Two diagonal rounded loops form a woven lattice at four shared integer crossings, with two short hanging ends replacing the fine tassel. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66f50153-1867-5790-86d6-291d9de28b8f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/chinese ornament_66f50153-1867-5790-86d6-291d9de28b8f.svg'
AUTHOR = 'gpt-6'

class ChineseEndlessKnot(Solo48):
    icon_id = 'chinese-endless-knot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/holidays"
    aliases = ()
    keywords = ('chinese', 'endless', 'knot')

    def build(self):
        for n,mirror in [('a',False),('b',True)]:
         def p(x,y):return (48-x,y) if mirror else (x,y)
         self.add_polyline(n+'-upper',p(14,6),p(24,16),p(32,24),p(38,30),p(38,34))
         self.add_arc(n+'-end',p(38,34),p(34,38),radius_x=4,sweep=not mirror)
         self.add_polyline(n+'-lower',p(34,38),p(30,38),p(24,32),p(16,24),p(6,14),p(6,10))
         self.add_arc(n+'-start',p(6,10),p(10,6),radius_x=4,sweep=not mirror)
         self.add_line(n+'-close',p(10,6),p(14,6))
         self.add_contour(n,*[n+f'-upper-{i}' for i in range(1,5)],n+'-end',*[n+f'-lower-{i}' for i in range(1,6)],n+'-start',n+'-close',closed=True)
         self.contours=[c for c in self.contours if c.contour_id not in [n+'-upper',n+'-lower']]
         self.add_line(n+'-tail',p(34,38),p(34,42));self.relate('connect',n,n+'-tail')
        self.relate('connect','a','b')
