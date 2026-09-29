"""car descending control.
Plan: Added an explicit sloped road beneath a recognizable side-view car with two round wheels.
Construction: car: coherent roof, hood, wheel arrangement.
Keyshape: SQUARE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '400b299b-3d6d-4ea5-900a-c45553cdafda'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-on-inclined-ramp/20260928T180129Z-thuan-mac/reference/car descending control_400b299b-3d6d-4ea5-900a-c45553cdafda.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'car-on-inclined-ramp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('car', 'descending', 'control')

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

        self.add_polyline('ramp',(4,44),(44,24))
        self.add_bezier('body',(9,31),((4,32),(3,29),(4,25)),((5,23),(7,22),(9,21)))
        self.add_polyline('roof',(9,21),(10,13),(24,6),(32,11))
        self.add_bezier('hood',(32,11),((36,8),(40,9),(42,13)),((44,17),(42,19),(39,20)))
        self.add_line('sill',(17,27),(29,21))
        self.circle('rear-wheel',13,29,4)
        self.circle('front-wheel',34,19,4)
        self.add_line('window-base',(9,21),(32,11))
        self.relate('connect','body','roof');self.relate('connect','roof','hood');self.relate('connect','roof','window-base')

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Preserve the reference diagonal car and separate sloped road. Compact wheel/body contacts and roof spacing keep the vehicle and incline legible.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '546bb4a5c5b131a3be65c53bba27e845315dbcd629b4c9c062c9bfe724b63fbb'}
