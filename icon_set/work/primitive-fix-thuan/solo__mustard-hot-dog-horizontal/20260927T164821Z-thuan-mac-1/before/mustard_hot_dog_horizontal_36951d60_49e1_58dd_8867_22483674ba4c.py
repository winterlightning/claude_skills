"""Hot Dog with Mustard.
Symbol plan: Horizontal rounded bun with wavy mustard edge across its exposed surface; bounds (4,10)-(44,38).
Construction reference: Supplied horizontal hot dog and Lucide sandwich: contrasting bread contours and filling edge.
Reduction: Extra narrow sausage-end loops omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36951d60-49e1-58dd-8867-22483674ba4c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/hot dog_36951d60-49e1-58dd-8867-22483674ba4c.svg'
AUTHOR = 'gpt-6'

class MustardHotDogHorizontal(Solo48):
    icon_id = 'mustard-hot-dog-horizontal'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('mustard', 'hot', 'dog', 'horizontal')

    def build(self):
        axis = 24  # Mirror pairs derive from a shared vertical axis.
        self.path('bun',(axis-8,10),[(axis+8,10),((axis+16,10),(axis+20,14),(axis+20,24)),((axis+20,34),(axis+16,38),(axis+8,38)),(axis-8,38),((axis-16,38),(axis-20,34),(axis-20,24)),((axis-20,14),(axis-16,10),(axis-8,10))],True)
        self.add_bezier('mustard',(axis-20,24),((axis-14,16),(axis-10,30),(axis-4,24)),((axis+2,18),(axis+6,30),(axis+12,24)),((axis+16,20),(axis+18,22),(axis+20,24)))
        self.relate('connect','mustard','bun')

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
