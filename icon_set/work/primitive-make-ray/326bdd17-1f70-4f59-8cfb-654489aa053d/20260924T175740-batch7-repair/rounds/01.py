from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='326bdd17-1f70-4f59-8cfb-654489aa053d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/pest busters_326bdd17-1f70-4f59-8cfb-654489aa053d.svg'
AUTHOR='gpt-6'
PLAN='A six-legged insect crossed by a diagonal pest-control slash.'
OMISSIONS='Thorax split and small head details omitted.'
LUCIDE_REFERENCE='bug'
HUMAN_REFERENCE=None
class Drawing(Solo48):
    icon_id='pest-busters'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/media'
    aliases=()
    keywords=('pest', 'busters')

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
        # One bug silhouette with head partition; slash shares exact body intersections.
        self.add_arc('head-top',(18,12),(30,12),radius_x=6)
        self.add_polyline('outline',(30,12),(30,16),(30,18),(34,24),(34,30),(32,36),(24,42),(16,36),(14,34),(14,24),(18,16),(18,12))
        self.relate('connect','head-top','outline')
        self.add_line('head-divider',(18,16),(30,16));self.relate('connect','head-divider','outline')
        self.add_polyline('slash',(6,42),(14,34),(30,18),(42,6));self.relate('connect','slash','outline')
        for n,a,z in [('left-front',(14,24),(6,20)),('right-front',(34,24),(42,24)),('left-back',(16,36),(6,40)),('right-back',(32,36),(42,40))]:
            self.add_line(n,a,z);self.relate('connect',n,'outline')
