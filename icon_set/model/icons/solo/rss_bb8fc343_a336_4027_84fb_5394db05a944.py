from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb8fc343-a336-4027-84fb-5394db05a944'
SOURCE_PATH = 'icon_set/work/todo-references/rss_bb8fc343-a336-4027-84fb-5394db05a944.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded RSS badge containing two broadcast quarter-circles and a circular dot.
# Reference: rss: concentric quarter-circle broadcasts around a bottom-left origin.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'rss'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('rss',)

    def build(self):
        self.add_line('top',(10,6),(14,6))
        self.add_arc('outer-curve',(14,6),(42,34),radius_x=28)
        self.add_line('right',(42,34),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left',(6,38),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('badge','top','outer-curve','right','br','bottom','bl','left','tl',closed=True)
        for n,r in [('large',20),('small',11)]: self.add_arc(n,(14,34-r),(14+r,34),radius_x=r)
        self.circle('dot',14,34,2)

    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self, n, l, t, r, b, q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
