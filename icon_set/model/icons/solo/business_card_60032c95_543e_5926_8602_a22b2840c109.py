from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '60032c95-543e-5926-8602-a22b2840c109'
SOURCE_PATH = 'pictographic-primitives/office/business card_60032c95-543e-5926-8602-a22b2840c109.svg'
AUTHOR = 'gpt-6'
PLAN = 'Business card with portrait and two text rules.'
CONSTRUCTION_REFERENCES = 'Lucide id-card: enclosure and text; human_ref/user.svg for portrait.'
OMISSIONS = 'Open shoulders replace the closed shirt outline.'

class Drawing(Solo48):
    icon_id = 'business-card'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('business', 'card')

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
        self.add_arc('shoulders',(x-4,top+4),(x+4,top+4),radius_x=4)
    def play(self,x,y,w,h):
        self.add_polyline('play',(x,y),(x+w,y+h//2),(x,y+h),closed=True)

    def build(self):
        self.box('card',6,6,36,36,3)
        self.person(19,18,3)
        for i,y in enumerate((19,27)):self.add_line('text-'+str(i),(31,y),(33,y))
