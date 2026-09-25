"""monitor letters, complete SOLO48 composition.
Symbol plan in build(); visible keyshape extremes (4, 4, 44, 44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dd80ecbb-13f8-47dc-9883-44bd19aa7cc6'
SOURCE_PATH = 'pictographic-primitives/other/monitor letters_dd80ecbb-13f8-47dc-9883-44bd19aa7cc6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'monitor-letters'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('monitor letters',)

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
        self.rounded('screen',8,4,32,32,3)
        self.add_line('stand',(24,36),(24,44))
        self.add_polyline('foot',(16,44),(24,44),(32,44))
        self.relate('connect','screen','stand');self.relate('connect','stand','foot')

    def banknote(self):
        self.add_polyline('note',(4,8),(44,8),(44,40),(4,40),closed=True)
        # Paired eight-unit corner quadrants meet the note edges.
        arcs=[((12,8),(4,16)),((44,16),(36,8)),((4,32),(12,40)),((36,40),(44,32))]
        for i,(a,b) in enumerate(arcs):
            self.add_arc('corner-'+str(i),a,b,radius_x=8)
            self.relate('connect','note','corner-'+str(i))

    def build(self):
        self.monitor()
        self.add_polyline('a',(12,28),(14,20),(16,12),(18,20),(20,28))
        self.add_line('a-bar',(14,20),(18,20));self.relate('connect','a','a-bar')
        self.add_polyline('b-stem',(24,12),(24,20),(24,28))
        self.add_line('b-top',(24,12),(28,12))
        self.add_arc('b-upper',(28,12),(28,20),radius_x=4)
        self.add_line('b-middle',(28,20),(24,20))
        self.add_arc('b-lower',(28,20),(28,28),radius_x=4)
        self.add_line('b-bottom',(28,28),(24,28))
        for n in ('b-top','b-middle','b-bottom'):self.relate('connect','b-stem',n)
        for a,b in [('b-top','b-upper'),('b-upper','b-middle'),('b-middle','b-lower'),('b-lower','b-bottom')]:self.relate('connect',a,b)
        self.add_arc('c',(36,14),(36,26),radius_x=6,large_arc=True,sweep=False)
