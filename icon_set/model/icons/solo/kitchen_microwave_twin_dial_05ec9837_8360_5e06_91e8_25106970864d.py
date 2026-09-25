"""Kitchen Microwave Oven.
Symbol plan: Wide rounded microwave, two feet, right control column. Plain broad door. Bounds (4,10)-(44,38).
Construction reference: Supplied microwave; Lucide microwave rounded case and attached feet.
Reduction: Dials and marks reduced to dots; feet share body nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05ec9837-8360-5e06-91e8-25106970864d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/microwave_05ec9837-8360-5e06-91e8-25106970864d.svg'
AUTHOR = 'gpt-6'

class KitchenMicrowaveTwinDial(Solo48):
    icon_id = 'kitchen-microwave-twin-dial'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('kitchen', 'microwave', 'twin', 'dial')

    def build(self):
        self.path('body',(8,10),[(26,10),(40,10),((42,10),(44,12),(44,14)),(44,30),((44,32),(42,36),(40,36)),(38,36),(26,36),(10,36),(8,36),((6,36),(4,32),(4,30)),(4,14),((4,12),(6,10),(8,10))],True)
        self.add_line('panel',(26,10),(26,36));self.relate('connect','panel','body')
        for x in (10,38):self.add_line('foot-'+str(x),(x,36),(x,38));self.relate('connect','foot-'+str(x),'body')
        for y in (19,27):self.add_dot('control-'+str(y),(35,y))

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
