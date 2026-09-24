from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fc535717-5e07-564a-aad9-923ace667ffb'
SOURCE_PATH = 'pictographic-primitives/holidays/star_fc535717-5e07-564a-aad9-923ace667ffb.svg'
AUTHOR = 'gpt-6'
PLAN = 'Award medal with inset star and notched ribbon.'
CONSTRUCTION_REFERENCES = 'Lucide star: alternating points and shared mirror axis.'
OMISSIONS = 'No omissions.'

class Drawing(Solo48):
    icon_id = 'star'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('star',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)
    def monitor(self):
        self.box('screen',6,6,36,28,3)
        self.add_line('stand',(24,34),(24,42))
        self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','screen','stand');self.relate('connect','stand','foot')
    def person(self,x,y,r):
        # human_ref/user.svg: head and broad shoulders. Exact 8 centerline / 4 ink gap.
        self.circle('head',x,y,r)
        top=y+r+8
        self.add_arc('shoulders',(x-5,top+5),(x+5,top+5),radius_x=5)
    def play(self,x,y,w,h):
        self.add_polyline('play',(x,y),(x+w,y+h//2),(x,y+h),closed=True)

    def build(self):
        # Rounded medal contour with explicit shared ribbon attachment nodes.
        self.add_bezier('medal',(24,4),((33,4),(40,11),(40,20)),((40,25),(39,29),(36,32)),((33,35),(28,36),(24,36)),((20,36),(15,35),(12,32)),((9,29),(8,25),(8,20)),((8,11),(15,4),(24,4)))
        self.add_polyline('star',(24,13),(26,17),(31,18),(27,22),(28,26),(24,24),(20,26),(21,22),(17,18),(22,17),closed=True)
        self.add_polyline('ribbon',(12,32),(12,44),(24,39),(36,44),(36,32))
        self.relate('connect','medal','ribbon')
