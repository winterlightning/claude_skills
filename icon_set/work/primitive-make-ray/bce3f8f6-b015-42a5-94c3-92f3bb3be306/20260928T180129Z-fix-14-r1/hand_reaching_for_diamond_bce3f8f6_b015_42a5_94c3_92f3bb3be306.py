"""diamond hold.
Plan: Restored the rounded index finger and thumb pinch, open wrist, and flat-topped diamond with a facet line.
Construction: hand-grab and gem: rounded finger return and flat-topped jewel.
Keyshape: SQUARE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'bce3f8f6-b015-42a5-94c3-92f3bb3be306'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-reaching-for-diamond/20260928T180129Z-thuan-mac/reference/diamond hold_bce3f8f6-b015-42a5-94c3-92f3bb3be306.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hand-reaching-for-diamond'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('diamond', 'hold')

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

        self.add_polyline('gem',(4,13),(8,6),(18,6),(23,13),(13,24),(4,13))
        self.add_line('facet',(4,13),(23,13));self.relate('connect','facet','gem')
        self.add_bezier('hand',(42,42),((42,34),(43,20),(38,13)),((35,9),(31,8),(28,8)),((24,8),(24,13),(28,13)),((34,13),(36,19),(34,24)),((32,31),(26,32),(22,27)),((18,21),(13,25),(17,30)),((21,35),(25,37),(25,42)))
