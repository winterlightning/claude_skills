"""ganesh chaturthi.
Plan: Restored broad elephant ears, rounded forehead lobes, separate crown, eyes, and a curved long trunk.
Construction: No useful deity match; paired geometry and smooth contour principles.
Keyshape: VRECT_L; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '13270d5a-f46a-55c2-a6f7-ca5c17dc5aa2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ganesha-head/20260928T180129Z-thuan-mac/reference/ganesh chaturthi_13270d5a-f46a-55c2-a6f7-ca5c17dc5aa2.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'ganesha-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('ganesh', 'chaturthi')

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

        self.add_bezier('crown',(15,14),((13,10),(18,5),(24,4)),((30,5),(35,10),(33,14)))
        self.add_bezier('face',(21,29),((12,27),(12,13),(19,13)),((22,13),(23,15),(24,15)),((25,15),(26,13),(29,13)),((37,13),(35,27),(30,29)),((27,31),(27,35),(28,36)),((30,37),(36,34),(36,38)),((36,42),(22,48),(21,39)),((21,36),(21,32),(21,29)))
        for side in [-1,1]:
         def p(x,y):return (24+side*x,y)
         self.add_bezier('ear'+str(side),p(10,15),(p(22,8),p(19,22),p(17,26)),(p(15,29),p(12,30),p(8,30)))
        self.add_dot('eye-left',(20,22));self.add_dot('eye-right',(28,22))

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Preserve the crowned elephant head, broad ears, eyes and curved trunk. Compact facial contacts and the natural silhouette are intentional.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': 'c41d2fc280b4433e6ef40bbbeb94df46a5e0b86af6d535a2cd91c9c3f63c65a4'}
