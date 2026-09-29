"""intersection assistant.
Plan: Restored branching intersection edges, paired sensor waves, and a larger rounded car.
Construction: car-front: rounded front body and tapered windscreen.
Keyshape: SQUARE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'ab4d1610-e735-4977-967a-897386cdcc6d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-intersection-sensor-waves/20260928T180129Z-thuan-mac/reference/intersection assistant_ab4d1610-e735-4977-967a-897386cdcc6d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'car-intersection-sensor-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('intersection', 'assistant')

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

        self.rect('body',14,27,20,11,3)
        self.add_polyline('roof',(16,27),(19,19),(29,19),(32,27))
        self.relate('connect','roof','body')
        for x in [18,30]:
         self.add_line('tire'+str(x),(x,38),(x,41));self.relate('connect','tire'+str(x),'body')
        for side in [-1,1]:
         def p(x,y):return (24+side*x,y)
         s=str(side)
         self.add_polyline('road'+s,p(18,42),p(14,23),p(18,23))
         self.add_bezier('wave-in'+s,p(7,8),(p(10,9),p(12,11),p(12,14)))
         self.add_bezier('wave-out'+s,p(9,4),(p(16,5),p(20,8),p(20,14)))

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Preserve two sensor-wave pairs, a visible windscreen and branching intersection corners; the road-to-car spacing and optical envelope remain readable at 48px.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': 'fb5eb77fa900ad5f54c61f7c470ea9c0decbd27017b4a3fb4850cae621033dab'}
