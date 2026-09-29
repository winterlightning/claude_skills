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

        self.add_bezier('orbit',(9,38),((0,29),(3,8),(17,5)),((32,0),(44,12),(44,24)),((44,30),(42,35),(39,38)))
        self.circle('earth',24,18,10)
        self.add_bezier('land-upper',(25,8),((19,14),(28,12),(27,19)),((27,24),(30,20),(34,18)))
        self.add_bezier('land-lower',(14,18),((21,16),(19,24),(23,28)))
        self.circle('node',24,40,4)
