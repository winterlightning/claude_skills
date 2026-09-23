from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef'
SOURCE_PATH='icon_set/work/todo-references/pesach passover 2_8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef.svg'
AUTHOR='gpt-6'
PLAN='Passover star on a round plate behind a segmented matzo tile.'
OMISSIONS='Tile rows reduced to one split; plate hidden behind foreground tile.'
LUCIDE_REFERENCE='star'
HUMAN_REFERENCE=None
class Drawing(Solo48):
    icon_id='pesach-passover-2'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/media'
    aliases=()
    keywords=('pesach', 'passover', '2')

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
        # Passover star on a round plate behind a segmented matzo tile.

        self.add_arc('plate',(22,38),(38,22),radius_x=16,large_arc=True)
        self.add_polyline('star',(22,12),(25,19),(32,20),(27,25),(28,32),(22,28),(16,32),(17,25),(12,20),(19,19),closed=True)
        self.box('tile',26,26,16,16,2)
        self.add_line('row',(26,34),(42,34));self.relate('connect','row','tile')

