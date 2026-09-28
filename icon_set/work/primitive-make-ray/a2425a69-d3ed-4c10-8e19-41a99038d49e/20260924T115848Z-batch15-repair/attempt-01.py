"""money bill pound, complete SOLO48 composition.
Symbol plan in build(); visible keyshape extremes (2, 6, 46, 42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a2425a69-d3ed-4c10-8e19-41a99038d49e'
SOURCE_PATH = 'icon_set/work/todo-references/money bill pound_a2425a69-d3ed-4c10-8e19-41a99038d49e.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'money-bill-pound'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('money bill pound',)

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
        arcs=[((16,8),(4,20)),((44,20),(32,8)),((4,28),(16,40)),((32,40),(44,28))]
        for i,(a,b) in enumerate(arcs):
            self.add_arc('corner-'+str(i),a,b,radius_x=12)
            self.relate('connect','note','corner-'+str(i))

    def build(self):
        # Banknote corner decoration and a hand-authored pound sterling symbol.
        self.banknote()
        self.add_arc('pound-hook',(30,21),(22,21),radius_x=4,sweep=False)
        self.add_line('pound-upper',(22,21),(22,23))
        self.add_line('pound-lower',(22,23),(22,27))
        self.add_arc('pound-curve',(22,27),(18,31),radius_x=4)
        self.add_line('pound-base',(18,31),(30,31))
        self.add_contour('pound','pound-hook','pound-upper','pound-lower','pound-curve','pound-base')
        self.add_polyline('pound-bar',(18,23),(22,23),(26,23))
        self.relate('connect','pound','pound-bar')
