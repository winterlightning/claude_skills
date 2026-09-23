"""A mobile phone displays a circled plus sign.
Construction reference: smartphone.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e101e849-9e14-4d6e-9afb-b2a07c50a1df'
SOURCE_PATH = 'icon_set/work/todo-references/mobile phone circle add_e101e849-9e14-4d6e-9afb-b2a07c50a1df.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-circle-add'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile', 'phone', 'circle', 'add')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
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

        # Shared symbol plan: upright phone, lower band, individually authored content.
        self.rect('phone',8,4,32,40)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')

        # Nested content symbol with centered plus.
        self.circle('add-circle',24,20,8)
        self.add_line('plus-h',(20,20),(28,20))
        self.add_line('plus-v',(24,16),(24,24))
        self.relate('connect','plus-h','plus-v')
