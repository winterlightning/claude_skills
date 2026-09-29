"""traveling on road.
Plan: Restored converging road edges, a dashed center line, and a rounded front car with lamps.
Construction: car-front: rounded bumper and windscreen.
Keyshape: VRECT_L; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '6991145f-84e0-41a4-b67e-a6f1b5dd5aba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-on-road/20260928T180129Z-thuan-mac/reference/traveling on road_6991145f-84e0-41a4-b67e-a6f1b5dd5aba.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'car-on-road'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('traveling', 'on', 'road')

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

        self.rect('body',8,16,32,14,3)
        self.add_polyline('roof',(11,16),(16,4),(32,4),(37,16));self.relate('connect','roof','body')
        for x in [14,34]:
         self.add_dot('lamp'+str(x),(x,23));self.add_line('tire'+str(x),(x,30),(x,32));self.relate('connect','tire'+str(x),'body')
        self.add_line('road-left',(12,39),(8,44));self.add_line('road-right',(36,39),(40,44))
        self.add_line('dash1',(24,36),(24,38));self.add_line('dash2',(24,43),(24,44))

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Retain two headlights, dashed center line and converging road edges beneath the car; these details are distinct at native size despite tighter spacing.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': 'bf701016ada0b9a90a639bc859d348f2804b49952209cf911406318843dc6056'}
