"""A mobile phone displaying moon icon.
Construction reference: moon.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f95043ca-40ab-49c2-a1e1-3374c581f165'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone moon_f95043ca-40ab-49c2-a1e1-3374c581f165.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-moon'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('mobile', 'phone', 'moon')

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

        # Closed crescent; intentional asymmetry is the moon phase.
        self.add_bezier('crescent',(30,13),((12,12),(12,28),(30,27)),((25,24),(25,17),(30,13)))
        self.add_contour('moon','crescent',closed=True)
