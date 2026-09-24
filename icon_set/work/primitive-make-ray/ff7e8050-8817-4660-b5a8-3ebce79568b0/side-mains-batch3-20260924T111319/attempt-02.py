from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ff7e8050-8817-4660-b5a8-3ebce79568b0'
SOURCE_PATH = 'pictographic-primitives/state/slash sperm_ff7e8050-8817-4660-b5a8-3ebce79568b0.svg'
AUTHOR = 'gpt-6'
PLAN = 'Sperm cell inside a slashed prohibition circle.'
CONSTRUCTION_REFERENCES = 'No useful Lucide match for the organic cell.'
OMISSIONS = 'Slash interrupted around the cell as in the reference.'

class Drawing(Solo48):
    icon_id = 'slash-sperm'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('slash', 'sperm')

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
        self.add_arc('ring-a',(12,40),(36,8),radius_x=20)
        self.add_arc('ring-b',(36,8),(12,40),radius_x=20)
        self.add_contour('ring','ring-a','ring-b',closed=True)
        self.add_line('slash-low',(12,40),(17,35));self.relate('connect','ring','slash-low')
        self.add_line('slash-high',(30,14),(36,8));self.relate('connect','ring','slash-high')
        self.add_bezier('cell',(16,15),((12,15),(14,24),(18,24)),((22,24),(25,19),(22,17)),((20,15),(18,15),(16,15)))
        self.add_bezier('tail',(18,24),((29,24),(30,28),(26,31)),((23,34),(27,35),(30,34)))
        self.relate('connect','cell','tail')
