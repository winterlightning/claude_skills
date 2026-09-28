"""hospital, re-authored as one complete SOLO48 composition.
Symbol plan is recorded in build(); paired shapes share dimensions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ac907133-ac86-5817-9678-483912faa2f6'
SOURCE_PATH = 'icon_set/work/todo-references/hospital_ac907133-ac86-5817-9678-483912faa2f6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hospital'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('hospital',)

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
        # Three-volume facade; 24-unit tower leaves eight-unit bands around door.
        self.add_polyline('tower',(12,40),(12,8),(36,8),(36,40))
        self.add_polyline('left-wing',(12,20),(4,20),(4,40),(12,40))
        self.add_polyline('right-wing',(36,20),(44,20),(44,40),(36,40))
        self.relate('connect','tower','left-wing')
        self.relate('connect','tower','right-wing')
        self.add_line('base',(12,40),(36,40))
        self.relate('connect','base','tower')
        self.add_polyline('door',(20,40),(20,32),(28,32),(28,40))
        self.relate('connect','base','door')
        self.add_line('cross-h',(20,20),(28,20))
        self.add_line('cross-v',(24,16),(24,24))
        self.relate('connect','cross-h','cross-v')

# Declared visible keyshape extremes: (2, 6, 46, 42).
