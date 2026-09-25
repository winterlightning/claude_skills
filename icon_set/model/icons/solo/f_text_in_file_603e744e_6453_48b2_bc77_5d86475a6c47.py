"""f text in file: reference reconstructed as a complete SOLO48 subject.
Plan: coherent contours and shared parameters; see build for symbol ownership.
Keyshape VRECT_L; visible extremes (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '603e744e-6453-48b2-bc77-5d86475a6c47'
SOURCE_PATH = 'icon_set/work/todo-references/f text in file_603e744e-6453-48b2-bc77-5d86475a6c47.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'f-text-in-file'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('f text in file',)

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
        # Tall document with clipped top corner and a single centerline letter F.
        self.add_line('top',(14,4),(30,4))
        self.add_line('clipped-corner',(30,4),(40,14))
        self.add_line('right',(40,14),(40,38))
        self.add_arc('br',(40,38),(34,44),radius_x=6)
        self.add_line('bottom',(34,44),(14,44))
        self.add_arc('bl',(14,44),(8,38),radius_x=6)
        self.add_line('left',(8,38),(8,10))
        self.add_arc('tl',(8,10),(14,4),radius_x=6)
        self.add_contour('page','top','clipped-corner','right','br','bottom','bl','left','tl',closed=True)
        self.add_polyline('letter-f',(29,16),(18,16),(18,34))
        self.add_line('f-middle',(18,25),(28,25))
        self.relate('connect','letter-f','f-middle')
