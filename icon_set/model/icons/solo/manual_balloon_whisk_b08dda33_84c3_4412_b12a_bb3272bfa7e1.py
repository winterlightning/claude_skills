"""Manual Kitchen Balloon Whisk.
Symbol plan: Diagonal balloon wires with smooth oval head and single-stroke grip. Bounds (6,6)-(42,42).
Construction reference: Supplied diagonal whisk; Lucide utensils continuous single grip.
Reduction: Wire array reduced to outer balloon and central wire; grip outline removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b08dda33-84c3-4412-b12a-bb3272bfa7e1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/whisk_b08dda33-84c3-4412-b12a-bb3272bfa7e1.svg'
AUTHOR = 'gpt-6'

class ManualBalloonWhisk(Solo48):
    icon_id = 'manual-balloon-whisk'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('manual', 'balloon', 'whisk')

    def build(self):
        self.path('wires',(20,28),[((15,19),(25,6),(35,6)),((37,6),(37,7),(39,9)),((41,11),(42,11),(42,13)),((42,23),(29,33),(20,28))],True)
        self.add_line('center',(20,28),(39,9));self.relate('connect','center','wires')
        self.add_line('grip',(6,42),(20,28));self.relate('connect','grip','wires');self.relate('connect','grip','center')

    def path(self, name, start, commands, closed=False):
        members=[]
        for j,c in enumerate(commands):
            tag=f'{name}-{j}'
            if len(c)==2:self.add_line(tag,start,c);start=c
            else:self.add_bezier(tag,start,c);start=c[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def loop(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-r',(x,y-ry),(x,y+ry),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-l',(x,y+ry),(x,y-ry),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-r',name+'-l',closed=True)

    def steam(self,x,top,bottom,name):
        mid=(top+bottom)//2
        self.add_bezier(name,(x+1,top),((x-2,top+2),(x-2,mid),(x,mid)),((x+2,mid),(x+2,bottom-2),(x-1,bottom)))
