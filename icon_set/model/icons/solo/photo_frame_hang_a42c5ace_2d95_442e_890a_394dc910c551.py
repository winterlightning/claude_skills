from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='a42c5ace-2d95-442e-890a-394dc910c551'
SOURCE_PATH='icon_set/work/todo-references/photo frame hang_a42c5ace-2d95-442e-890a-394dc910c551.svg'
AUTHOR='gpt-6'
PLAN='A hanging double frame contains a tower and stepped buildings.'
OMISSIONS='Tower crossbeam omitted; two building steps retained.'
LUCIDE_REFERENCE='image'
HUMAN_REFERENCE=None
class Drawing(Solo48):
    icon_id='photo-frame-hang'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'images'
    aliases=()
    keywords=('photo', 'frame', 'hang')

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
        # A hanging double frame contains a tower and stepped buildings.

        self.add_polyline('hanger',(15,14),(24,6),(33,14))
        self.add_polyline('frame',(6,14),(15,14),(33,14),(42,14),(42,42),(6,42),closed=True)
        self.relate('connect','hanger','frame')
        self.add_polyline('inner',(13,21),(35,21),(35,35),(13,35),closed=True)
        self.add_polyline('tower',(15,35),(21,23),(27,35));self.relate('connect','tower','inner')
        self.add_polyline('buildings',(28,35),(28,30),(31,30),(31,26),(35,26));self.relate('connect','buildings','inner')

