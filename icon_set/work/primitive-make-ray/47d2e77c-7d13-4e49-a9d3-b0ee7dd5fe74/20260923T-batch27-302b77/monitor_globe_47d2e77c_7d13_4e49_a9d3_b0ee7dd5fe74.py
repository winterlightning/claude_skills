"""monitor globe, complete SOLO48 composition.
Symbol plan in build(); visible keyshape extremes (4, 4, 44, 44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '47d2e77c-7d13-4e49-a9d3-b0ee7dd5fe74'
SOURCE_PATH = 'icon_set/work/todo-references/monitor globe_47d2e77c-7d13-4e49-a9d3-b0ee7dd5fe74.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'monitor-globe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('monitor globe',)

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
        # Globe with center meridian and two parallels; circular silhouette.
        self.monitor()
        self.circle('globe',24,20,10)
        self.add_line('meridian',(24,10),(24,30))
        self.relate('connect','globe','meridian')
        for i,y in enumerate((14,26)):
            self.add_line('parallel-'+str(i),(16,y),(32,y))
            self.relate('connect','globe','parallel-'+str(i))
            self.relate('connect','meridian','parallel-'+str(i))
