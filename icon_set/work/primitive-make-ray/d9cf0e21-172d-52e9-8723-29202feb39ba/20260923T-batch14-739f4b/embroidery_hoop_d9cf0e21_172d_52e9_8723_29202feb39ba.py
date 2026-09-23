"""embroidery hoop: reference reconstructed as a complete SOLO48 subject.
Plan: coherent contours and shared parameters; see build for symbol ownership.
Keyshape VRECT_L; visible extremes (6,2)-(42,46).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd9cf0e21-172d-52e9-8723-29202feb39ba'
SOURCE_PATH = 'icon_set/work/todo-references/embroidery hoop_d9cf0e21-172d-52e9-8723-29202feb39ba.svg'
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
        # One broad clamp grows out of the hoop; inner ring repeats its center.
        self.add_line('neck-left',(16,4),(16,16))
        self.add_arc('shoulder-left',(16,16),(8,28),radius_x=8,radius_y=12,sweep=False)
        self.add_arc('lower-ring',(8,28),(40,28),radius_x=16,sweep=False)
        self.add_arc('shoulder-right',(40,28),(32,16),radius_x=8,radius_y=12,sweep=False)
        self.add_line('neck-right',(32,16),(32,4))
        self.add_line('clamp-top',(32,4),(16,4))
        self.add_contour('hoop','neck-left','shoulder-left','lower-ring','shoulder-right','neck-right','clamp-top',closed=True)
        self.circle('inner-ring',24,28,7)
        self.add_line('screw',(32,8),(40,8))
        self.add_line('screw-head',(40,4),(40,12))
        self.relate('connect','screw','screw-head')
