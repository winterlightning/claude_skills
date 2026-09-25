"""A mobile phone displays a capital F.
Construction reference: smartphone.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0045f15c-b131-434f-9f5d-bf6646957611'
SOURCE_PATH = 'icon_set/work/todo-references/mobile phone f text_0045f15c-b131-434f-9f5d-bf6646957611.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-f-text'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('mobile', 'phone', 'f', 'text')

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

        # Shared F stem with top and middle arms, open on the right.
        self.add_polyline('f',(18,28),(18,13),(30,13))
        self.add_line('f-middle',(18,21),(28,21))
        self.relate('connect','f','f-middle')
