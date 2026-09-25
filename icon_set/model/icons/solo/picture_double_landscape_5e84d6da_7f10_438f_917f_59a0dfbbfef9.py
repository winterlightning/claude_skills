from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='5e84d6da-7f10-438f-917f-59a0dfbbfef9'
SOURCE_PATH='icon_set/work/todo-references/picture double landscape_5e84d6da-7f10-438f-917f-59a0dfbbfef9.svg'
AUTHOR='gpt-6'
PLAN='Two overlapping landscape cards with mountains in the foreground.'
OMISSIONS='Rear card content is hidden; mountain baseline omitted and slopes extended to the frame edges to enlarge both peaks.'
LUCIDE_REFERENCE='gallery-vertical-end'
HUMAN_REFERENCE=None
class Drawing(Solo48):
    icon_id='picture-double-landscape'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('picture', 'double', 'landscape')

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
        # Two overlapping landscape cards with mountains in the foreground.

        self.add_polyline('rear',(6,33),(6,6),(33,6))
        self.box('front',15,15,27,27,3)
        self.add_polyline('mountains',(15,34),(25,24),(31,31),(35,27),(42,34));self.relate('connect','mountains','front')

