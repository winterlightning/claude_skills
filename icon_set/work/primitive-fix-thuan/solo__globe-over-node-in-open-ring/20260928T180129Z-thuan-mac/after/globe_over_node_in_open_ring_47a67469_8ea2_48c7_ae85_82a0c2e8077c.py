"""amazon web service cross region data delivery 1.
Plan: Enlarged the earth and node while keeping a clean open surrounding ring and readable continent strokes.
Construction: globe: circular global silhouette; source continent arrangement preserved.
Keyshape: CIRCLE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '47a67469-8ea2-48c7-ae85-82a0c2e8077c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__globe-over-node-in-open-ring/20260928T180129Z-thuan-mac/reference/amazon web service cross region data delivery 1_47a67469-8ea2-48c7-ae85-82a0c2e8077c.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'globe-over-node-in-open-ring'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('amazon', 'web', 'service', 'cross', 'region', 'data', 'delivery', '1')

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
        self.add_arc('orbit',(8,36),(40,36),radius_x=20,large_arc=True,sweep=True)
        self.circle('earth',24,20,10)
        self.add_polyline('north-land',(24,10),(22,15),(25,18),(32,18))
        self.add_polyline('south-land',(15,22),(21,22),(24,29))
        self.circle('node',24,40,4)

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Preserve a clear circular earth with simplified land boundaries above a separate node inside the open orbit. Nested globe details require reduced clearance.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '4e2e71b44643c6c0edd3868198898170d9206336afee9f298a253c40595e66cd'}
