"""Peeled Rambutan Fruit.
Symbol plan: Exposed front fruit in hairy peel and partial rear shell. Bounds (6,6)-(42,42).
Construction reference: Supplied rambutan; no useful direct Lucide match.
Reduction: Numerous short hairs reduced to five; small face marks omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45e656c6-4bca-50f1-b21e-8bc009cccead'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/rambutan peeled_45e656c6-4bca-50f1-b21e-8bc009cccead.svg'
AUTHOR = 'gpt-6'

class PeeledRambutanFruit(Solo48):
    icon_id = 'peeled-rambutan-fruit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('peeled', 'rambutan', 'fruit')

    def build(self):
        self.path('rear',(18,26),[((8,26),(6,22),(6,16)),((6,13),(8,11),(10,10)),((12,8),(14,6),(16,6)),((22,6),(28,10),(28,16))])
        self.path('front',(18,26),[((18,20),(22,16),(28,16)),((34,16),(38,20),(38,26)),((38,30),(36,33),(34,35)),((32,37),(30,38),(28,38)),((24,38),(22,36),(20,34)),((18,32),(18,30),(18,26))],True);self.relate('connect','front','rear')
        self.add_line('peel',(18,26),(38,26));self.relate('connect','peel','front');self.relate('connect','peel','rear')
        for j,(a,b,owner) in enumerate([((10,10),(6,6),'rear'),((38,26),(42,26),'front'),((34,35),(38,39),'front'),((28,38),(28,42),'front'),((20,34),(16,38),'front')]):
         self.add_line('hair-'+str(j),a,b);self.relate('connect','hair-'+str(j),owner)
         if a==(38,26):self.relate('connect','hair-'+str(j),'peel')

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
