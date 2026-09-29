"""chip hold.
Plan: Separated a four-sided chip with multiple pins from a recognizable index-thumb pinch and open wrist.
Construction: hand-grab: rounded finger turns and coherent palm; human_ref/user.svg reviewed.
Keyshape: SQUARE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '7fbc0ada-902f-43f4-bdab-cc7b8ccc1b02'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-pinching-chip/20260928T180129Z-thuan-mac/reference/chip hold_7fbc0ada-902f-43f4-bdab-cc7b8ccc1b02.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hand-pinching-chip'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('chip', 'hold')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.rect('chip',6,13,11,11,2)
        for i in range(2):
         t=9+i*5
         for n,a,b in [('t',(t,10),(t,13)),('b',(t,24),(t,27)),('l',(3,16+i*5),(6,16+i*5)),('r',(17,16+i*5),(20,16+i*5))]:self.add_line(n+str(i),a,b)
        self.add_bezier('hand',(42,42),((42,34),(42,26),(40,22)),((36,17),(29,8),(24,6)),((21,6),(21,12),(24,12)),((26,12),(28,12),(30,14)),((35,19),(34,25),(31,27)),((26,32),(22,26),(20,24)),((17,21),(14,23),(16,27)),((20,33),(28,36),(28,42)))
