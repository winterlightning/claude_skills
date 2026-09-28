"""mobile phone unlock: complete SOLO48 repair.
Kept a visibly open shackle, open lock body, and lower phone bezel.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b0d42cd4-6acc-4018-ae89-490f3eb333a9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-phone-unlock/20260927T142540Z-thuan-mac-1/reference/mobile phone unlock_b0d42cd4-6acc-4018-ae89-490f3eb333a9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-unlock'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
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

        # Open lock body and a raised, deliberately unlatched shackle.
        self.add_polyline('lock-body',(18,21),(18,27),(30,27),(30,21))
        self.add_line('shackle-stem',(18,21),(18,17))
        self.add_arc('shackle-bend',(18,17),(22,13),radius_x=4)
        self.add_line('shackle-tip',(22,13),(28,13))
        self.add_contour('open-shackle','shackle-stem','shackle-bend','shackle-tip')
        self.relate('connect','lock-body','open-shackle')
        self.add_line('lower-bezel',(8,36),(40,36))
        self.relate('connect','phone','lower-bezel')
