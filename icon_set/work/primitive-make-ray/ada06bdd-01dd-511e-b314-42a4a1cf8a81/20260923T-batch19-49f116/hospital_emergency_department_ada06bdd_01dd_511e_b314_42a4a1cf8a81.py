"""hospital emergency department, re-authored as one complete SOLO48 composition.
Symbol plan is recorded in build(); paired shapes share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ada06bdd-01dd-511e-b314-42a4a1cf8a81'
SOURCE_PATH = 'icon_set/work/todo-references/hospital emergency department_ada06bdd-01dd-511e-b314-42a4a1cf8a81.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hospital-emergency-department'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('hospital emergency department',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)

    def rounded(self,n,x,y,w,h,r):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=points[i],points[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)

    def heart(self):
        # Paired nine-unit lobes and mirrored lower shoulders.
        self.add_arc('left-lobe',(24,15),(6,15),radius_x=9,sweep=False)
        self.add_arc('left-shoulder',(6,15),(10,25),radius_x=14,sweep=False)
        self.add_line('point-1',(10,25),(24,42))
        self.add_line('point-2',(24,42),(38,25))
        self.add_arc('right-shoulder',(38,25),(42,15),radius_x=14,sweep=False)
        self.add_arc('right-lobe',(42,15),(24,15),radius_x=9,sweep=False)
        self.add_contour('heart','left-lobe','left-shoulder','point-1','point-2','right-shoulder','right-lobe',closed=True)

    def build(self):
        # Centered raised emergency sign, building wings and open doorway.
        self.rounded('sign',13,6,22,22,4)
        self.add_line('cross-horizontal',(22,17),(26,17))
        self.add_line('cross-vertical',(24,15),(24,19))
        self.relate('connect','cross-horizontal','cross-vertical')
        self.add_polyline('building',(13,18),(6,18),(6,42),(18,42),(18,34),(30,34),(30,42),(42,42),(42,18),(35,18))
        self.relate('connect','sign','building')
        self.add_line('baseline',(6,42),(42,42))
        self.relate('connect','building','baseline')

# Declared visible keyshape extremes: (4, 4, 44, 44).
