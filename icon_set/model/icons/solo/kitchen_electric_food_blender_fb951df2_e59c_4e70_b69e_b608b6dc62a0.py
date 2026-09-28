"""Kitchen Electric Food Blender.
Symbol plan: Tapered jug and flared base share lower nodes; lid at4. Bounds (8,4)-(40,44).
Construction reference: Supplied food blender; Lucide blender tapered jug and flared base.
Reduction: Blade and tiny button outline omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb951df2-e59c-4e70-b69e-b608b6dc62a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/blender_fb951df2-e59c-4e70-b69e-b608b6dc62a0.svg'
AUTHOR = 'gpt-6'

class KitchenElectricFoodBlender(Solo48):
    icon_id = 'kitchen-electric-food-blender'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('kitchen', 'electric', 'food', 'blender')

    def build(self):
        self.path('jug',(8,12),[(12,4),(36,4),(40,12),(33,26),(15,26),(8,12)],True)
        self.add_line('lid',(8,12),(40,12));self.relate('connect','lid','jug')
        self.path('base',(15,26),[(10,40),((9,43),(10,44),(13,44)),(35,44),((38,44),(39,43),(38,40)),(33,26)]);self.relate('connect','base','jug')
        self.add_dot('control',(24,35))

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
