"""Kitchen Utensil Soup Ladle.
Symbol plan: Wide low bowl and gently leaning hook shaft. Bounds (8,4)-(40,44).
Construction reference: Supplied sloping ladle; Lucide soup semicircular bowl and utensils single stems.
Reduction: Handle side edges replaced by one smooth hooked stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a733702-7b07-51aa-aae9-13c9578de92a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/ladle_2a733702-7b07-51aa-aae9-13c9578de92a.svg'
AUTHOR = 'gpt-6'

class KitchenUtensilLadle(Solo48):
    icon_id = 'kitchen-utensil-ladle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('kitchen', 'utensil', 'ladle')

    def build(self):
        self.add_arc('bowl',(8,33),(28,33),radius_x=10,radius_y=11,sweep=False)
        self.add_line('rim',(8,33),(28,33));self.relate('connect','bowl','rim')
        self.path('handle',(28,33),[(30,11),((30,7),(32,4),(35,4)),((38,4),(40,7),(40,11)),(40,13)]);self.relate('connect','handle','bowl');self.relate('connect','handle','rim')

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
