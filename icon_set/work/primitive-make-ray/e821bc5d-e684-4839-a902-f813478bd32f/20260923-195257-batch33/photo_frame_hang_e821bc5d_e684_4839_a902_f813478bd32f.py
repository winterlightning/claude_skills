from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='e821bc5d-e684-4839-a902-f813478bd32f'
SOURCE_PATH='icon_set/work/todo-references/photo frame hang_e821bc5d-e684-4839-a902-f813478bd32f.svg'
AUTHOR='gpt-6'
PLAN='A hanging picture shows a central tower flanked by two trees.'
OMISSIONS='Tower crossbar retained; leaf interiors omitted.'
LUCIDE_REFERENCE='image'
HUMAN_REFERENCE=None
class Drawing(Solo48):
    icon_id='photo-frame-hang'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/media'
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
        # A hanging picture shows a central tower flanked by two trees.

        self.add_polyline('hanger',(15,15),(24,6),(33,15))
        self.box('frame',6,15,36,27,4);self.relate('connect','hanger','frame')
        self.add_polyline('tower',(17,34),(24,21),(31,34))
        self.add_line('beam',(21,27),(27,27))
        for name,x in [('left',12),('right',36)]:
            self.add_bezier(name,(x,27),((x-5,32),(x-3,35),(x,35)),((x+3,35),(x+5,32),(x,27)))

