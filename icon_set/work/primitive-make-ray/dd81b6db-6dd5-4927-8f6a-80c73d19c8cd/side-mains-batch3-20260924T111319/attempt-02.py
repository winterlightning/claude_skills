from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dd81b6db-6dd5-4927-8f6a-80c73d19c8cd'
SOURCE_PATH = 'pictographic-primitives/messages/messages bubble square question_dd81b6db-6dd5-4927-8f6a-80c73d19c8cd.svg'
AUTHOR = 'gpt-6'
PLAN = 'Square speech bubble containing a question mark.'
CONSTRUCTION_REFERENCES = 'Lucide monitor enclosure principle; question and tail authored directly.'
OMISSIONS = 'No omissions.'

class Drawing(Solo48):
    icon_id = 'messages-bubble-square-question'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('messages', 'bubble', 'square', 'question')

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
        self.add_polyline('bubble',(9,6),(39,6),(42,9),(42,35),(39,38),(24,38),(16,42),(16,38),(9,38),(6,35),(6,9),closed=True)
        self.add_arc('question-top',(20,19),(28,19),radius_x=4)
        self.add_arc('question-hook',(28,19),(24,23),radius_x=4)
        self.add_contour('question','question-top','question-hook')
        self.add_dot('question-dot',(24,31))
