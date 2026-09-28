"""Kitchen Soup Ladle.
Symbol plan: Deep semicircular bowl with rim and tall hooked handle. Bounds (8,4)-(40,44).
Construction reference: Supplied upright ladle; Lucide soup bowl construction and utensils single-stroke stems.
Reduction: Slender handle reduced to a single continuous stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe979308-9012-51b0-937b-16e29b4b1983'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/scooper_fe979308-9012-51b0-937b-16e29b4b1983.svg'
AUTHOR = 'gpt-6'

class KitchenSoupLadleUpright(Solo48):
    icon_id = 'kitchen-soup-ladle-upright'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('kitchen', 'soup', 'ladle', 'upright')

    def build(self):
        self.add_arc('bowl',(8,33),(30,33),radius_x=11,sweep=False)
        self.add_line('rim',(8,33),(30,33));self.relate('connect','bowl','rim')
        self.add_line('shaft',(30,33),(30,9));self.add_arc('hook',(30,9),(40,9),radius_x=5)
        self.add_line('tip',(40,9),(40,14));self.add_contour('handle','shaft','hook','tip');self.relate('connect','handle','bowl');self.relate('connect','handle','rim')

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
