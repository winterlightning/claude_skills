from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='05a94426-1cba-44df-a701-8939c33872de'
SOURCE_PATH='icon_set/work/todo-references/photo crop rotate_05a94426-1cba-44df-a701-8939c33872de.svg'
AUTHOR='gpt-6'
PLAN='Crop corners surrounded by two curved rotation arrows.'
OMISSIONS='Rotation arcs simplified to quarter circles.'
LUCIDE_REFERENCE='crop'
HUMAN_REFERENCE=None
class Drawing(Solo48):
    icon_id='photo-crop-rotate'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/media'
    aliases=()
    keywords=('photo', 'crop', 'rotate')

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
        # Crop corners surrounded by two curved rotation arrows.

        self.add_polyline('crop-left',(15,10),(15,33),(38,33))
        self.add_polyline('crop-right',(10,15),(33,15),(33,38))
        self.relate('connect','crop-left','crop-right')
        self.add_arc('rotate-top',(26,6),(42,22),radius_x=16)
        self.add_polyline('top-head',(32,6),(26,6),(26,12));self.relate('connect','rotate-top','top-head')
        self.add_arc('rotate-bottom',(22,42),(6,26),radius_x=16)
        self.add_polyline('bottom-head',(16,42),(22,42),(22,36));self.relate('connect','rotate-bottom','bottom-head')

