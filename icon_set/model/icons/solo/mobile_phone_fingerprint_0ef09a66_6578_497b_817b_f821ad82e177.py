"""A mobile phone displays a fingerprint.
Construction reference: smartphone.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0ef09a66-6578-497b-817b-f821ad82e177'
SOURCE_PATH = 'icon_set/work/todo-references/mobile phone fingerprint_0ef09a66-6578-497b-817b-f821ad82e177.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-fingerprint'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile', 'phone', 'fingerprint')

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

        # Smooth nested ridge curves; intentional asymmetry follows fingertip flow.
        self.add_arc('outer-ridge',(16,20),(32,20),radius_x=8)
        self.add_bezier('inner-ridge',(16,27),((24,24),(17,16),(24,16)),((30,16),(25,25),(32,29)))
        self.add_bezier('left-tail',(24,22),((24,26),(21,28),(20,30)))
        self.add_bezier('right-tail',(25,28),((26,30),(27,31),(28,32)))
