"""monitor payment, complete SOLO48 composition.
Symbol plan in build(); visible keyshape extremes (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '68edf9b6-f133-45a4-a6a6-b6d0df318a0c'
SOURCE_PATH = 'icon_set/work/todo-references/monitor payment_68edf9b6-f133-45a4-a6a6-b6d0df318a0c.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'monitor-payment'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ()
    keywords = ('monitor payment',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)

    def rounded(self,n,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)

    def monitor(self):
        # Symmetric rounded screen, split bottom edge at actual stand attachment.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,30))
        self.add_arc('br',(42,30),(38,34),radius_x=4)
        self.add_line('bottom-right',(38,34),(24,34))
        self.add_line('bottom-left',(24,34),(10,34))
        self.add_arc('bl',(10,34),(6,30),radius_x=4)
        self.add_line('left',(6,30),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('screen','top','tr','right','br','bottom-right','bottom-left','bl','left','tl',closed=True)
        self.add_line('stand',(24,34),(24,42))
        self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','screen','stand')
        self.relate('connect','stand','foot')

    def banknote(self):
        self.add_polyline('note',(4,8),(44,8),(44,40),(4,40),closed=True)
        # Paired eight-unit corner quadrants meet the note edges.
        arcs=[((12,8),(4,16)),((44,16),(36,8)),((4,32),(12,40)),((36,40),(44,32))]
        for i,(a,b) in enumerate(arcs):
            self.add_arc('corner-'+str(i),a,b,radius_x=8)
            self.relate('connect','note','corner-'+str(i))

    def build(self):
        # Empty monitor with a flared payment-terminal pedestal.
        self.rounded('screen',6,6,36,24,4)
        self.add_arc('pedestal-left',(20,30),(14,40),radius_x=6,radius_y=10)
        self.add_line('foot-left',(14,40),(14,42))
        self.add_line('foot',(14,42),(34,42))
        self.add_line('foot-right',(34,42),(34,40))
        self.add_arc('pedestal-right',(34,40),(28,30),radius_x=6,radius_y=10)
        self.add_contour('pedestal','pedestal-left','foot-left','foot','foot-right','pedestal-right')
        self.relate('connect','screen','pedestal')
