"""Revision of the claimed reference after comparing original and rejected drawing."""
"""mobile phone lock: complete SOLO48 repair.
Enlarged the lock body and shackle opening. Removed the lower phone divider.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '26319804-c7ff-498f-a76f-62441d482fc8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-phone-lock/20260927T142529Z-thuan-mac-1/reference/mobile phone lock_26319804-c7ff-498f-a76f-62441d482fc8.svg'
AUTHOR = "gpt-6"
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
        # The bottom phone band and clear lock body follow the reference.
        self.rect('phone',8,4,32,40)
        self.add_line('bezel',(8,36),(40,36)); self.relate('connect','phone','bezel')
        self.add_polyline('lock-body',(20,20),(17,20),(17,28),(31,28),(31,20),(28,20))
        self.add_line('shackle-left',(20,20),(20,17))
        self.add_arc('shackle-top',(20,17),(28,17),radius_x=4)
        self.add_line('shackle-right',(28,17),(28,20))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','shackle','lock-body')
