"""Kitchen Spatula Scraper.
Symbol plan: Asymmetric broad scraper blade tapering to rounded grip. Bounds (10,4)-(38,44).
Construction reference: Supplied scraper; Lucide paintbrush-vertical for broad head tapering to slim grip.
Reduction: No blade surface decoration; intentional unequal shoulders retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a39c0ccd-17e0-5071-98fc-ec9b0889d2f0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/spatula scraper_a39c0ccd-17e0-5071-98fc-ec9b0889d2f0.svg'
AUTHOR = 'gpt-6'

class KitchenSpatulaScraper(Solo48):
    icon_id = 'kitchen-spatula-scraper'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('kitchen', 'spatula', 'scraper')

    def build(self):
        self.path('outline',(16,4),[(34,4),((38,4),(38,7),(38,10)),(34,20),((33,23),(28,25),(28,28)),(28,40),((28,42),(26,44),(24,44)),((22,44),(20,42),(20,40)),(20,28),((20,25),(10,24),(10,18)),(12,8),((12,5),(13,4),(16,4))],True)

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
