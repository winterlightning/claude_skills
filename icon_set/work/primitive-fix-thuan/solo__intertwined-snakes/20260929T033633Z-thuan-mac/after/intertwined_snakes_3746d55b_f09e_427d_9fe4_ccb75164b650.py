"""snakes.
Plan: Restored four pointed snake heads around a rotationally repeated curved interweave.
Construction: No useful exact snake match; four quarter-turn instances share smooth S-body geometry.
Keyshape: SQUARE; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '3746d55b-f09e-427d-9fe4-ccb75164b650'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__intertwined-snakes/20260929T033633Z-thuan-mac/reference/snakes_3746d55b-f09e-427d-9fe4-ccb75164b650.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'intertwined-snakes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('snakes',)

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
        # Two offset serpentine bodies preserve the intertwined-snakes concept at native size.
        self.add_bezier('snake-left',(12,15),((0,21),(10,31),(24,31)),((40,31),(41,44),(26,44)))
        self.add_bezier('head-left',(12,15),((7,11),(11,6),(17,7)),((20,7),(20,5),(22,4)),((23,12),(19,18),(12,15)))
        self.add_bezier('snake-right',(36,18),((44,26),(31,28),(25,22)),((13,9),(4,20),(7,29)),((9,34),(13,36),(17,36)))
        self.add_bezier('head-right',(36,18),((31,15),(33,8),(36,7)),((40,6),(42,11),(41,15)),((41,17),(43,18),(44,20)),((40,21),(38,20),(36,18)))
        self.relate('connect','snake-left','head-left');self.relate('connect','snake-right','head-right')

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Retain two recognizable pointed snake heads, long serpentine tails and offset intertwined coils. Simplify the four-head reference motif to two snakes for clear native-size reading; preserve natural shape and compact head joins.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '3d4c49bd9bfa78cc4c14f69a28c6c7242cb654f3e3a6ac232ae8fbf67d2f2d03'}
