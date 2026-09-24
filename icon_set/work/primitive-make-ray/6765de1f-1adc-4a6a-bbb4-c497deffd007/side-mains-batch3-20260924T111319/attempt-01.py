from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6765de1f-1adc-4a6a-bbb4-c497deffd007'
SOURCE_PATH = 'pictographic-primitives/other/ui webpage social profile_6765de1f-1adc-4a6a-bbb4-c497deffd007.svg'
AUTHOR = 'gpt-6'
PLAN = 'Social profile webpage with header marks, portrait and text.'
CONSTRUCTION_REFERENCES = 'Lucide id-card: portrait and text; human_ref/user.svg for head and shoulders.'
OMISSIONS = 'Header dashes become dots; no semantic components omitted.'

class Drawing(Solo48):
    icon_id = 'ui-webpage-social-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('ui', 'webpage', 'social', 'profile')

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
        self.box('page',6,6,36,36,3)
        self.add_line('header',(6,16),(42,16));self.relate('connect','page','header')
        for i,x in enumerate((14,22,30)):self.add_dot('header-dot-'+str(i),(x,11))
        self.person(17,25,3)
        for i,y in enumerate((27,35)):self.add_line('text-'+str(i),(30,y),(34,y))
