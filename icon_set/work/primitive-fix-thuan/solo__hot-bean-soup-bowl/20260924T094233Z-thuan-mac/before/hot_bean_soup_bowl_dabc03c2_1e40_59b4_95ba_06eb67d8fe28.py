"""Hot Bowl of Bean Soup.
Symbol plan: Broad open bowl with one large kidney bean, two steam wisps. Bounds (4,8)-(44,40).
Construction reference: Lucide soup for bowl and wisps; supplied reference for bean on open surface.
Reduction: Two beans reduced to one recognizable kidney bean; rear rim and foot omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dabc03c2-1e40-59b4-95ba-06eb67d8fe28'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/bean soup_dabc03c2-1e40-59b4-95ba-06eb67d8fe28.svg'
AUTHOR = 'gpt-6'

class HotBeanSoupBowl(Solo48):
    icon_id = 'hot-bean-soup-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('hot', 'bean', 'soup', 'bowl')

    def build(self):
        self.path('bowl',(4,22),[((4,34),(14,40),(24,40)),((34,40),(44,34),(44,22))])
        self.path('bean',(22,20),[((27,18),(31,21),(31,25)),((31,30),(25,32),(21,29)),((17,26),(23,25),(20,22)),((19,21),(20,20),(22,20))],True)
        for i,x in enumerate((12,38)):self.steam(x,8,14,f'steam-{i}')

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
