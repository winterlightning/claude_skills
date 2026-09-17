"""Manual Garlic Press.
Symbol plan: Deep left chamber and two diverging levers. Bounds (6,6)-(42,42); diagonal upper lever gives clear hinge opening.
Construction reference: Supplied garlic press; Lucide utensils simple handles.
Reduction: Handle outlines, tiny hinge and perforations omitted; deep chamber and open handles retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ebce9ec7-a9df-5567-8163-797ad5eaaee5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/garlic mincer_ebce9ec7-a9df-5567-8163-797ad5eaaee5.svg'
AUTHOR = 'gpt-6'

class ManualGarlicPress(Solo48):
    icon_id = 'manual-garlic-press'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('manual', 'garlic', 'press')

    def build(self):
        self.path('cup',(6,26),[(22,26),(20,38),((20,41),(18,42),(14,42)),(12,42),((8,42),(6,40),(6,36)),(6,26)],True)
        self.add_line('lower',(22,26),(42,26));self.relate('connect','lower','cup')
        self.add_line('upper',(6,26),(32,6));self.relate('connect','upper','cup')

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
