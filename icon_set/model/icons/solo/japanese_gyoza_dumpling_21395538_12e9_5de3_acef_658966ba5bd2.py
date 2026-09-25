"""Japanese Gyoza Dumpling.
Symbol plan: Broad dumpling pouch and three radial crimp folds, mirror axis24. Bounds (4,10)-(44,38).
Construction reference: Supplied pleated gyoza; Lucide cooking-pot for smooth broad food silhouette.
Reduction: Five lobes reduced to three pleats.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21395538-12e9-5de3-acef-658966ba5bd2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/gyoza grill deep fried dumpling_21395538-12e9-5de3-acef-658966ba5bd2.svg'
AUTHOR = 'gpt-6'

class JapaneseGyozaDumpling(Solo48):
    icon_id = 'japanese-gyoza-dumpling'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('japanese', 'gyoza', 'dumpling')

    def build(self):
        self.path('body',(4,28),[((4,20),(8,16),(12,14)),((16,11),(20,10),(24,10)),((28,10),(32,11),(36,14)),((40,16),(44,20),(44,28)),((44,35),(35,38),(24,38)),((13,38),(4,35),(4,28))],True)
        self.path('seam',(4,28),[((8,25),(12,24),(16,23)),((19,22),(21,22),(24,22)),((27,22),(29,22),(32,23)),((36,24),(40,25),(44,28))]);self.relate('connect','seam','body')
        for j,(a,b) in enumerate([((12,14),(16,23)),((24,10),(24,22)),((36,14),(32,23))]):
         self.add_line('fold-'+str(j),a,b);self.relate('connect','fold-'+str(j),'body');self.relate('connect','fold-'+str(j),'seam')

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
