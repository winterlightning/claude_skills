"""expand 5: reference reconstructed as a complete SOLO48 subject.
Plan: coherent contours and shared parameters; see build for symbol ownership.
Keyshape SQUARE; visible extremes (4,4)-(44,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3e282822-91f6-475d-8f28-cb58fc1bbac5'
SOURCE_PATH = 'icon_set/work/todo-references/expand 5_3e282822-91f6-475d-8f28-cb58fc1bbac5.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'expand-5'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('expand 5',)

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
        # Center square with four reflected outward corner arrows.
        self.rounded('center-square',18,18,12,12,3)
        for i,(sx,sy) in enumerate(((-1,-1),(1,-1),(-1,1),(1,1))):
            corner=(24+18*sx,24+18*sy)
            self.add_polyline('arrow-'+str(i),(24+10*sx,corner[1]),corner,(corner[0],24+10*sy))
            self.add_line('shaft-'+str(i),(24+12*sx,24+12*sy),corner)
            self.relate('connect','arrow-'+str(i),'shaft-'+str(i))
