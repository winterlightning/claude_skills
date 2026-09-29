"""squarespace logo.
Plan: Restored broad diagonal S ribbons with rounded returns and overlapping offset ends.
Construction: No useful exact Lucide logo match; coherent tangent curves and shared diagonal offsets.
Keyshape: SQUARE; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'e67f8d26-5a13-4179-830d-68e3d196c80a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__interlocking-s-emblem/20260929T033633Z-thuan-mac/reference/squarespace logo_e67f8d26-5a13-4179-830d-68e3d196c80a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'interlocking-s-emblem'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('squarespace', 'logo')

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
        self.add_bezier('ribbon',(36,8),((33,5),(30,5),(27,8)),((27,3),(20,2),(16,6)),((12,10),(8,14),(6,18)),((0,27),(11,36),(19,29)),((24,24),(29,19),(32,17)),((40,11),(49,21),(44,30)),((40,35),(35,41),(32,43)),((28,46),(25,44),(24,42)))
        self.add_bezier('return',(24,42),((29,37),(34,32),(38,28)),((42,24),(37,20),(34,24)),((29,29),(24,34),(20,38)),((16,42),(12,41),(10,39)))
        self.relate('connect','ribbon','return')

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Retain the source emblem broad diagonal ribbons, upper notch and rounded inner return. Natural optical bounds and compact parallel returns are intentional, with the previously pinched opening enlarged.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': 'f582150a8575a91ec24655ec9ed6f69e2c3e0aed2554bca55b766773a3574415'}
