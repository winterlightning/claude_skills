"""Kitchen Microwave Oven.
Symbol plan: Rounded almost-square case, high window, one control, shared foot nodes. Bounds (6,6)-(42,42).
Construction reference: Lucide microwave original and atomic geometry: rounded housing, inset window, short feet. Supplied reference for square proportions.
Reduction: Narrow panel seam omitted; one control reduced to a dot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3586c98-a8cf-43e1-a70d-94f10260a501'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/vending machine_e3586c98-a8cf-43e1-a70d-94f10260a501.svg'
AUTHOR = 'gpt-6'

class KitchenMicrowaveSquareWindow(Solo48):
    icon_id = 'kitchen-microwave-square-window'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('kitchen', 'microwave', 'square', 'window')

    def build(self):
        self.path('case',(10,6),[(38,6),((40,6),(42,8),(42,10)),(42,34),((42,36),(40,38),(38,38)),(34,38),(14,38),(10,38),((8,38),(6,36),(6,34)),(6,10),((6,8),(8,6),(10,6))],True)
        self.path('window',(17,15),[(22,15),((24,15),(24,15),(24,17)),(24,24),((24,26),(24,26),(22,26)),(17,26),((15,26),(15,26),(15,24)),(15,17),((15,15),(15,15),(17,15))],True)
        self.add_dot('control',(33,15))
        for x in (14,34):self.add_line('foot-'+str(x),(x,38),(x,42));self.relate('connect','foot-'+str(x),'case')

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
