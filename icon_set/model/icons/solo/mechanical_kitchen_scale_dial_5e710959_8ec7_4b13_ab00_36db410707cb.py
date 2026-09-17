"""Mechanical Kitchen Scale.
Symbol plan: Arched tapered weighing body, concentric central dial and upright needle. Bounds (8,4)-(40,44).
Construction reference: Supplied mechanical scale; Lucide citrus concentric radial structure.
Reduction: Outer tick ring and bottom decorative line omitted for a clear dial.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e710959-8ec7-4b13-ab00-36db410707cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/tools kitchen scale_5e710959-8ec7-4b13-ab00-36db410707cb.svg'
AUTHOR = 'gpt-6'

class MechanicalKitchenScaleDial(Solo48):
    icon_id = 'mechanical-kitchen-scale-dial'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('mechanical', 'kitchen', 'scale', 'dial')

    def build(self):
        axis=24
        self.path('body',(axis,4),[((34,4),(40,12),(40,23)),(36,40),((36,43),(35,44),(32,44)),(16,44),((13,44),(12,43),(12,40)),(8,23),((8,12),(14,4),(axis,4))],True)
        self.loop('dial',axis,23,7)
        self.add_line('needle',(axis,16),(axis,23));self.relate('connect','needle','dial')

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
