"""Kitchen Food Scale.
Symbol plan: Wide weighing bowl above tapered base and circular dial. Bounds (8,4)-(40,44).
Construction reference: Supplied mechanical scale; Lucide weight tapered base.
Reduction: Dial needle omitted; dial retained as compact circular aperture.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e83c9dc8-80c1-469c-a231-60c3c6870730'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/tools kitchen scale 1_e83c9dc8-80c1-469c-a231-60c3c6870730.svg'
AUTHOR = 'gpt-6'

class KitchenFoodScale(Solo48):
    icon_id = 'kitchen-food-scale'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('kitchen', 'food', 'scale')

    def build(self):
        self.path('bowl',(8,4),[(40,4),((38,10),(32,12),(24,12)),((16,12),(10,10),(8,4))],True)
        self.add_line('neck',(24,12),(24,22));self.relate('connect','neck','bowl')
        self.path('base',(24,22),[(35,22),(40,44),(8,44),(13,22),(24,22)],True);self.relate('connect','neck','base')
        self.loop('dial',24,33,2)

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
