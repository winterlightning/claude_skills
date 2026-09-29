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

        self.add_polyline('mouthpiece',(10,4),(16,4))
        self.add_bezier('outer',(16,4),((23,4),(25,9),(25,17)))
        self.add_line('inner-shaft',(16,4),(16,31))
        self.add_bezier('bow-outer',(16,31),((16,48),(35,48),(35,31)))
        self.add_polyline('bell',(35,31),(38,25),(29,17),(29,30))
        self.add_bezier('bow-inner',(29,30),((29,36),(25,36),(25,30)))
        self.add_line('shaft',(25,30),(25,17))
        for y in [17,24]:self.add_line('key'+str(y),(22,y),(27,y))
        self.relate('connect','outer','mouthpiece');self.relate('connect','outer','inner-shaft');self.relate('connect','inner-shaft','bow-outer');self.relate('connect','bow-outer','bell');self.relate('connect','bell','bow-inner');self.relate('connect','bow-inner','shaft');self.relate('connect','shaft','outer')
