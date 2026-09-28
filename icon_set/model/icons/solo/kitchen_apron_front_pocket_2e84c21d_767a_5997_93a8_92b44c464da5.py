"""Kitchen Apron with Front Pocket.
Symbol plan: Symmetric apron with neck strap and broad pocket. Bounds (8,4)-(40,44).
Construction reference: Supplied apron; no useful direct Lucide match.
Reduction: Loose side ties omitted; neck loop and pocket retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e84c21d-767a-5997-93a8-92b44c464da5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear apron_2e84c21d-767a-5997-93a8-92b44c464da5.svg'
AUTHOR = 'gpt-6'

class KitchenApronFrontPocket(Solo48):
    icon_id = 'kitchen-apron-front-pocket'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('kitchen', 'apron', 'front', 'pocket')

    def build(self):
        self.path('body',(16,14),[((16,18),(12,20),(8,20)),(8,40),((8,43),(9,44),(12,44)),(36,44),((39,44),(40,43),(40,40)),(40,20),((36,20),(32,18),(32,14)),(16,14)],True)
        self.path('neck',(16,14),[(16,12),((16,7),(19,4),(24,4)),((29,4),(32,7),(32,12)),(32,14)]);self.relate('connect','neck','body')
        self.path('pocket',(17,26),[(31,26),(31,29),((31,33),(28,35),(24,35)),((20,35),(17,33),(17,29)),(17,26)],True)

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
