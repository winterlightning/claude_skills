"""mobile phone unlock: complete SOLO48 repair.
Kept the lock body and visibly open shackle; lowered the shackle arc and removed the phone divider.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b0d42cd4-6acc-4018-ae89-490f3eb333a9'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone unlock_b0d42cd4-6acc-4018-ae89-490f3eb333a9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-unlock'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile', 'phone', 'unlock')

    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: rounded upright phone and lower band; content owns its own geometry.
        self.rect('phone',8,4,32,40)

        self.rect('lock-body',18,23,12,8)
        self.add_line('shackle-stem',(20,23),(20,17))
        self.add_arc('shackle-cap',(20,17),(28,17),radius_x=4)
        self.add_contour('open-shackle','shackle-stem','shackle-cap')
        self.relate('connect','open-shackle','lock-body')
