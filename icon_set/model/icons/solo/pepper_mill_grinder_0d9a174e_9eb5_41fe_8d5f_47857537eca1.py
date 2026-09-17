"""Pepper Mill Grinder.
Symbol plan: Turned concave mill with cap and rounded top collar; axis24. Bounds (10,4)-(38,44).
Construction reference: Supplied pepper mill; no direct useful Lucide match.
Reduction: Base collar seam omitted; cap, upper collar and concave waist retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d9a174e-9eb5-41fe-8d5f-47857537eca1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/seasoning pepper ground_0d9a174e-9eb5-41fe-8d5f-47857537eca1.svg'
AUTHOR = 'gpt-6'

class PepperMillGrinder(Solo48):
    icon_id = 'pepper-mill-grinder'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('pepper', 'mill', 'grinder')

    def build(self):
        self.path('collar',(14,12),[(18,12),(30,12),(34,12),((39,12),(39,20),(34,20)),(14,20),((9,20),(9,12),(14,12))],True)
        self.add_polyline('cap',(18,12),(18,4),(30,4),(30,12));self.relate('connect','cap','collar')
        self.path('body',(14,20),[((20,30),(18,38),(10,44)),(38,44),((30,38),(28,30),(34,20))]);self.relate('connect','body','collar')

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
