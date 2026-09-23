from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='2776d1bd-8c4b-4ccf-9408-3e6584f12510'
SOURCE_PATH='icon_set/work/todo-references/phone control application_2776d1bd-8c4b-4ccf-9408-3e6584f12510.svg'
AUTHOR='gpt-6'
PLAN='A horizontal wireless phone controller with two equal round buttons.'
OMISSIONS='Narrow right seam and second wireless arc omitted to preserve clearance.'
LUCIDE_REFERENCE=None
HUMAN_REFERENCE=None
class Drawing(Solo48):
    icon_id='phone-control-application'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/media'
    aliases=()
    keywords=('phone', 'control', 'application')

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
        # A horizontal wireless phone controller with two equal round buttons.

        self.box('controller',6,18,36,24,4)
        for i,x in enumerate((17,31)):self.circle('button'+str(i),x,30,2)
        self.add_arc('wireless',(18,8),(30,8),radius_x=6,radius_y=2)

