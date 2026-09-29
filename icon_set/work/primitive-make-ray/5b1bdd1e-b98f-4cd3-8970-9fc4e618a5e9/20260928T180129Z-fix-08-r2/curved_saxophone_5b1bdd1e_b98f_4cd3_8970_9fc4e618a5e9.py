"""instrument saxophone.
Plan: Slimmed the long body and retained a curved lower bow, flared upward bell, mouthpiece, and two keys.
Construction: No direct useful saxophone match; smooth arc and tangent principles used.
Keyshape: VRECT_M; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '5b1bdd1e-b98f-4cd3-8970-9fc4e618a5e9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curved-saxophone/20260928T180129Z-thuan-mac/reference/instrument saxophone_5b1bdd1e-b98f-4cd3-8970-9fc4e618a5e9.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'curved-saxophone'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('instrument', 'saxophone')

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

        self.add_line('mouthpiece',(10,4),(16,4))
        self.add_bezier('outer-neck',(16,4),((22,4),(24,9),(24,15)))
        self.add_line('shaft',(16,4),(16,31))
        self.add_bezier('outer-bow',(16,31),((16,48),(38,48),(38,30)))
        self.add_polyline('bell',(38,30),(40,25),(32,17),(32,31))
        self.add_bezier('inner-bow',(32,31),((32,37),(24,37),(24,31)))
        self.add_line('inner-shaft',(24,15),(24,31))
        for y in [16,24]:self.add_line('key'+str(y),(22,y),(26,y))
        self.relate('connect','outer-neck','mouthpiece');self.relate('connect','shaft','mouthpiece');self.relate('connect','shaft','outer-bow');self.relate('connect','outer-bow','bell');self.relate('connect','bell','inner-bow');self.relate('connect','inner-bow','inner-shaft');self.relate('connect','inner-shaft','outer-neck')

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Retain a slim saxophone shaft, separated inner bend, upward bell and two keys. Optical silhouette fit and compact bell spacing preserve the recognizable instrument.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '554664b9d89aa489b44288e1f669e98ed496c2125d4a620a8621b68459e82c5e'}
