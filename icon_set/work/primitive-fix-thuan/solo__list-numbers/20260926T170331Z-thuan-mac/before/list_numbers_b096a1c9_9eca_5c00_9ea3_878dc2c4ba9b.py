from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b096a1c9-9eca-5c00-9ea3-878dc2c4ba9b'
SOURCE_PATH = 'pictographic-primitives/interface-essential/list numbers_b096a1c9-9eca-5c00-9ea3-878dc2c4ba9b.svg'
AUTHOR = 'gpt-6'
PLAN = 'Numbered list with rows one, two and three.'
CONSTRUCTION_REFERENCES = 'Lucide list-ordered: numeral column and repeated rules.'
OMISSIONS = 'Compact monoline numerals.'

class Drawing(Solo48):
    icon_id = 'list-numbers'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "other", "primitives-generate")
    aliases = ()
    keywords = ('list', 'numbers')

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
        # Taller list gives each numeral eight units and two full inter-row gaps.
        self.add_polyline('one',(8,6),(12,4),(12,10))
        self.add_bezier('two-top',(8,20),((14,17),(19,21),(14,24)))
        self.add_polyline('two-base',(14,24),(8,29),(16,29));self.relate('connect','two-top','two-base')
        self.add_bezier('three',(8,37),((17,37),(17,40),(12,40)),((17,40),(17,44),(8,44)))
        for i,y in enumerate((8,24,40)):self.add_line('row-'+str(i),(26,y),(40,y))
