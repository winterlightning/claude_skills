from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '703647aa-6053-5e38-b352-06e55bc0fb70'
SOURCE_PATH = 'pictographic-primitives/protection/protection shield_703647aa-6053-5e38-b352-06e55bc0fb70.svg'
AUTHOR = 'gpt-6'
PLAN = 'Protection shield with a check mark.'
CONSTRUCTION_REFERENCES = 'Lucide shield: mirrored shoulders and lower bowl.'
OMISSIONS = 'No omissions.'

class Drawing(Solo48):
    icon_id = 'protection-shield'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('protection', 'shield')

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
        self.add_bezier('shield',(24,4),((19,8),(13,10),(8,10)),((8,26),(8,35),(24,44)),((40,35),(40,26),(40,10)),((35,10),(29,8),(24,4)))
        self.add_polyline('check',(17,24),(22,29),(31,20))
