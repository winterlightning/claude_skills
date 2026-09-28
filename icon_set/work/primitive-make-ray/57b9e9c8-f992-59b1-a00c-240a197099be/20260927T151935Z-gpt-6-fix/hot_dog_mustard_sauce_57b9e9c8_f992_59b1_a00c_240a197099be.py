"""Hot Dog with Mustard Sauce.
Symbol plan: Shallow upward-tilted hot dog and flowing mustard; bounds (4,8)-(44,40).
Construction reference: Supplied mustard hot dog; Lucide sandwich: one coherent food silhouette.
Reduction: Secondary bun seams omitted; shallow rising direction and mustard retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '57b9e9c8-f992-59b1-a00c-240a197099be'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hot-dog-mustard-sauce/20260927T151732Z-thuan-mac-1/reference/hot dog sausage_57b9e9c8-f992-59b1-a00c-240a197099be.svg'
AUTHOR = "gpt-6"

class HotDogMustardSauce(Solo48):
    icon_id = 'hot-dog-mustard-sauce'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('hot', 'dog', 'mustard', 'sauce')

    def build(self):
        self.path('bun',(4,28),[((4,22),(8,18),(14,16)),(30,9),((32,8),(34,8),(36,8)),((42,8),(44,12),(44,18)),((44,24),(40,28),(34,30)),(18,37),((16,39),(12,40),(10,40)),((6,40),(4,36),(4,28))],True)
        # A longer three-turn stripe follows the sausage's diagonal.
        self.add_bezier('mustard',(15,28),((18,30),(18,24),(22,25)),
                        ((25,28),(26,19),(30,21)),
                        ((33,23),(32,17),(35,19)))

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
