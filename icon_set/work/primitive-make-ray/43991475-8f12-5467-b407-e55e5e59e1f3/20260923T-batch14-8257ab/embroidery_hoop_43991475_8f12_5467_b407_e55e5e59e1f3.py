"""embroidery hoop: reference reconstructed as a complete SOLO48 subject.
Plan: coherent contours and shared parameters; see build for symbol ownership.
Keyshape VRECT_L; visible extremes (6,2)-(42,46).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '43991475-8f12-5467-b407-e55e5e59e1f3'
SOURCE_PATH = 'icon_set/work/todo-references/embroidery hoop_43991475-8f12-5467-b407-e55e5e59e1f3.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'embroidery-hoop'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('embroidery hoop',)

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, x, y, w, h, r):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=points[i],points[(i+1)%8]
            if i%2:self.add_arc(name+str(i),a,b,radius_x=r)
            else:self.add_line(name+str(i),a,b)
        self.add_contour(name,*(name+str(i) for i in range(8)),closed=True)

    def build(self):
        # Two concentric rings; split clamp has paired ears and a horizontal screw.
        self.circle('outer-hoop',24,28,16)
        self.circle('inner-hoop',24,28,7)
        for x in (20,28):
            self.add_line('ear-'+str(x),(x,4),(x,12))
        self.add_line('screw',(20,4),(36,4))
        for x in (20,28):self.relate('connect','ear-'+str(x),'screw')
