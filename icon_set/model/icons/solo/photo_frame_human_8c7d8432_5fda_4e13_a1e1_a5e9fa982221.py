from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='8c7d8432-5fda-4e13-a1e1-a5e9fa982221'
SOURCE_PATH='icon_set/work/todo-references/photo frame human_8c7d8432-5fda-4e13-a1e1-a5e9fa982221.svg'
AUTHOR='gpt-6'
PLAN='A framed abstract human profile with an eye above a nose and chin.'
OMISSIONS='Eyelashes reduced to a central brow tick; nested frame retained.'
LUCIDE_REFERENCE=None
HUMAN_REFERENCE='icon_set/references/human_ref/user.svg'
class Drawing(Solo48):
    icon_id='photo-frame-human'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'photography'
    categories = ('photography', 'primitives')
    aliases=()
    keywords=('photo', 'frame', 'human')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(pts):
            b=pts[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2:self.add_arc(name,a,b,radius_x=r)
            else:self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)

    def handset(self):
        # One coherent side-profile receiver: round outer sweep and two ear pads.
        self.add_bezier('receiver',(9,6),((6,6),(6,12),(6,15)),((6,26),(22,42),(33,42)),((37,42),(42,40),(42,37)),((42,35),(36,30),(34,30)),((32,30),(30,34),(28,32)),((22,28),(19,25),(16,20)),((14,17),(19,15),(19,12)),((19,10),(12,6),(9,6)))

    def build(self):
        # A framed abstract human profile with an eye above a nose and chin.

        self.box('frame',8,4,32,40,2)
        self.add_polyline('inner',(16,12),(32,12),(32,36),(16,36),closed=True)
        self.add_bezier('eye',(19,20),((22,16),(27,16),(30,20)),((27,23),(22,23),(19,20)))
        self.add_line('pupil',(25,18),(25,22))
        self.add_polyline('profile',(21,26),(18,30),(23,30),(22,33),(26,33),(27,36));self.relate('connect','profile','inner')

