"""Hot Bibimbap Bowl with Chopsticks.
Symbol plan: Bowl under an egg with two parallel chopsticks entering from right, one left steam curl. Bounds (6,6)-(42,42).
Construction reference: Lucide soup: broad bowl and steam; source bibimbap: central egg and right chopsticks.
Reduction: Fine food partitions and yolk omitted; two steam trails reduced to one longer curl.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78cb6741-967d-51b4-87f8-0ab4cef7536f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/kaream bibimbap_78cb6741-967d-51b4-87f8-0ab4cef7536f.svg'
AUTHOR = 'gpt-6'

class HotBibimbapChopsticks(Solo48):
    icon_id = 'hot-bibimbap-chopsticks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('hot', 'bibimbap', 'chopsticks')

    def build(self):
        self.path('bowl',(6,26),[(8,26),(24,26),(34,26),(42,26),((42,37),(34,42),(24,42)),((14,42),(6,37),(6,26))],True)
        self.add_arc('egg-left',(8,26),(16,18),radius_x=8)
        self.add_arc('egg-right',(16,18),(24,26),radius_x=8)
        self.add_contour('egg','egg-left','egg-right')
        self.relate('connect','egg','bowl')
        self.steam(8,6,12,'steam')
        self.add_line('stick-a',(24,26),(34,6))
        self.add_line('stick-b',(34,26),(42,10))
        for a,b in [('stick-a','bowl'),('stick-b','bowl'),('stick-a','egg')]:self.relate('connect',a,b)

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
