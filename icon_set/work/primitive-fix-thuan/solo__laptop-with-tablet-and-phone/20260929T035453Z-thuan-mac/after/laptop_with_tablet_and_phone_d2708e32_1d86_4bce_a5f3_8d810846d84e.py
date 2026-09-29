from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd2708e32-1d86-4bce-a5f3-8d810846d84e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__laptop-with-tablet-and-phone/20260929T035453Z-thuan-mac/reference/responsive design laptop_d2708e32-1d86-4bce-a5f3-8d810846d84e.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore two upright devices, the phone control, a partially occluded laptop screen and a downward notch in its base.
# Construction references: Lucide laptop: rounded upright screen and lower deck; source owns the two foreground devices and occlusion.
class Drawing(Solo48):
    icon_id = 'laptop-with-tablet-and-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'websites'
    aliases = ()
    keywords = ('responsive design laptop',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,x,y,w,h,r=0):
        if not r:
            self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for j in range(8):
            if j%2:self.add_arc(n+str(j),pts[j],pts[(j+1)%8],radius_x=r)
            else:self.add_line(n+str(j),pts[j],pts[(j+1)%8])
        self.add_contour(n,*(n+str(j) for j in range(8)),closed=True)
    def curve(self,n,start,*segments):
        self.add_bezier(n,start,*segments)

    def build(self):
        self.rect('tablet',13,4,13,25,3)
        self.rect('phone',33,4,12,25,3)
        self.add_dot('phone-control',(39,24))
        self.curve('laptop-left',(9,22),((6,22),(6,24),(6,27)),((6,27),(6,39),(6,39)))
        self.add_line('laptop-right',(41,33),(41,39))
        self.curve('base',(4,39),((4,44),(8,44),(12,44)),((12,44),(36,44),(36,44)),((40,44),(44,44),(44,39)))
        self.add_polyline('deck-left',(4,39),(18,39))
        self.curve('notch',(18,39),((18,43),(29,43),(29,39)))
        self.add_line('deck-right',(29,39),(44,39))
        self.relate('connect','base','deck-left');self.relate('connect','base','deck-right')
        self.relate('connect','notch','deck-left');self.relate('connect','notch','deck-right')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The original three-device composition needs compact screen placement, a small phone control and a shallow notched laptop base. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '6f74ab341af3285bd2c26a73a5e5dda5954a42bced29e1427ecae22ff1bf1f3a'}
