from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='ea43c7c4-27f8-52b3-94cb-d0a6f393aeca'
SOURCE_PATH='icon_set/work/todo-references/photo video editing_ea43c7c4-27f8-52b3-94cb-d0a6f393aeca.svg'
AUTHOR='gpt-6'
PLAN='A video preview bubble with play triangle above timeline trim controls.'
OMISSIONS='Timeline ticks reduced to two handles.'
LUCIDE_REFERENCE=None
HUMAN_REFERENCE=None
class Drawing(Solo48):
    icon_id='photo-video-editing'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/media'
    aliases=()
    keywords=('photo', 'video', 'editing')

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
        # A video preview bubble with play triangle above timeline trim controls.

        self.add_polyline('preview',(6,6),(42,6),(42,30),(29,30),(24,34),(19,30),(6,30),closed=True)
        self.add_polyline('play',(19,14),(19,22),(28,18),closed=True)
        self.add_line('timeline',(6,42),(42,42))
        for i,x in enumerate((14,34)):
            self.add_line('handle'+str(i),(x,38),(x,42));self.relate('connect','handle'+str(i),'timeline')

