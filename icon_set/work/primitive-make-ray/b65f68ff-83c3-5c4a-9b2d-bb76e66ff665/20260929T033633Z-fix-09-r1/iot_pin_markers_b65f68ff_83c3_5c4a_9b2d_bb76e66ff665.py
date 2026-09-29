"""internet of thing analytics services.
Plan: Restored a prominent upper node, a vertical link, and three small circular markers on diamond bases.
Construction: network: shared linked-node construction; original diamond map bases retained.
Keyshape: VRECT_L; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'b65f68ff-83c3-5c4a-9b2d-bb76e66ff665'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__iot-pin-markers/20260929T033633Z-thuan-mac/reference/internet of thing analytics services_b65f68ff-83c3-5c4a-9b2d-bb76e66ff665.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'iot-pin-markers'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('internet', 'of', 'thing', 'analytics', 'services')

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

        self.circle('hub',24,11,8)
        self.add_line('link',(24,19),(24,31));self.relate('connect','hub','link')
        for i,(x,y) in enumerate([(8,28),(24,34),(40,28)]):
         self.circle('marker'+str(i),x,y,3)
         self.add_polyline('base'+str(i),(x,y+3),(x+6,y+7),(x,y+11),(x-6,y+7),closed=True)
         self.relate('connect','marker'+str(i),'base'+str(i))
        self.relate('connect','link','marker1')

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve the prominent hub, vertical link, and three circular markers on true diamond bases. Compact pin/base junctions and small diamond interiors are essential semantic cues.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '0b5bb609839c68e7686d54eb638051743d25f38ca8fafcc81be1a5197badce5d'}
