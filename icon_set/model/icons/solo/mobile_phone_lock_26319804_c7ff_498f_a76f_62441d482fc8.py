"""mobile phone lock: complete SOLO48 repair.
Enlarged the lock body and shackle opening. Removed the lower phone divider.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '26319804-c7ff-498f-a76f-62441d482fc8'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone lock_26319804-c7ff-498f-a76f-62441d482fc8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-lock'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('mobile', 'phone', 'lock')

    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            elif name=='lock-body' and i==0:
                self.add_line(n+'a',a,(20,24));self.add_line(n+'b',(20,24),(28,24));self.add_line(n+'c',(28,24),b)
                names.extend([n+'a',n+'b',n+'c']);continue
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: rounded upright phone and lower band; content owns its own geometry.
        self.rect('phone',8,4,32,40)

        # Rounded body and tangent shackle, with exact shared attachment endpoints.
        self.rect('lock-body',17,24,14,10)
        self.add_line('shackle-left',(20,24),(20,17))
        self.add_arc('shackle-top',(20,17),(28,17),radius_x=4)
        self.add_line('shackle-right',(28,17),(28,24))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','shackle','lock-body')
