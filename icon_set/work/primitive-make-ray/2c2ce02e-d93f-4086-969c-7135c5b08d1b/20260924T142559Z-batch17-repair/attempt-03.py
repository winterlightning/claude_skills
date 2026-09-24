from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2c2ce02e-d93f-4086-969c-7135c5b08d1b'
SOURCE_PATH = 'pictographic-primitives/other/self payment computer dollar_2c2ce02e-d93f-4086-969c-7135c5b08d1b.svg'
AUTHOR = 'gpt-6'
PLAN = 'Payment monitor with dollar sign and two menu rules.'
CONSTRUCTION_REFERENCES = 'Lucide monitor: screen and stand.'
OMISSIONS = 'Compact currency glyph; no semantic omissions.'

class Drawing(Solo48):
    icon_id = 'self-payment-computer-dollar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('self', 'payment', 'computer', 'dollar')

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
        self.add_polyline('screen',(8,4),(40,4),(40,36),(24,36),(8,36),closed=True)
        self.add_line('stand',(24,36),(24,44))
        self.add_polyline('foot',(16,44),(24,44),(32,44))
        self.relate('connect','screen','stand');self.relate('connect','stand','foot')
        self.add_bezier('dollar-cap',(24,14),((23,13),(21,13),(20,13)))
        self.add_bezier('dollar-upper',(20,13),((16,13),(16,19),(20,20)))
        self.add_bezier('dollar-lower',(20,20),((24,21),(24,27),(20,27)))
        self.add_bezier('dollar-foot',(20,27),((19,27),(17,27),(17,26)))
        self.add_contour('dollar','dollar-cap','dollar-upper','dollar-lower','dollar-foot')
        self.add_line('stem-top',(20,12),(20,13))
        self.add_line('stem-bottom',(20,27),(20,28))
        self.relate('connect','dollar','stem-top');self.relate('connect','dollar','stem-bottom')
        for i,y in enumerate((16,24)):self.add_dot('menu-'+str(i),(32,y))
