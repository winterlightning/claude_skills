"""A mobile phone displaying pin icon.
Construction reference: map-pin.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd3023f2-6462-458d-9f32-0ee54bf229c9'
SOURCE_PATH = 'icon_set/work/todo-references/mobile phone pin_cd3023f2-6462-458d-9f32-0ee54bf229c9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-pin'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('mobile', 'phone', 'pin')

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

        # Plan: rounded upright phone and lower band; content owns its own geometry.
        self.rect('phone',8,4,32,40)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')

        # Rounded pin crown tapers smoothly to the centered point.
        self.add_arc('pin-crown',(17,20),(31,20),radius_x=7)
        self.add_bezier('pin-tip',(31,20),((31,23),(27,27),(24,28)),((21,27),(17,23),(17,20)))
        self.add_contour('pin','pin-crown','pin-tip',closed=True)
