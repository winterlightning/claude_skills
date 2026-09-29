"""workflow scrum.
Plan: Restored two circular iteration sweeps with separate arrowheads over a rightward baseline arrow.
Construction: No useful exact workflow match; coherent circular sweeps and open arrowheads.
Keyshape: VRECT_L; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '2d6aea0f-956f-475c-983c-4883f1ff0ac5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__iterative-workflow-arrows/20260929T033633Z-thuan-mac/reference/workflow scrum_2d6aea0f-956f-475c-983c-4883f1ff0ac5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'iterative-workflow-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('workflow', 'scrum')

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

        self.add_line('baseline',(4,42),(44,42));self.add_polyline('baseline-arrow',(39,37),(44,42),(39,47));self.relate('connect','baseline','baseline-arrow')
        self.add_bezier('lower-loop',(23,42),((38,34),(29,17),(17,21)),((9,23),(6,28),(7,33)))
        self.add_polyline('lower-arrow',(6,27),(7,33),(12,29));self.relate('connect','lower-loop','lower-arrow');self.relate('connect','lower-loop','baseline')
        self.add_bezier('upper-loop',(18,21),((5,13),(17,0),(27,5)),((33,7),(35,11),(34,16)))
        self.add_polyline('upper-arrow',(29,11),(34,16),(39,11));self.relate('connect','upper-loop','upper-arrow')
