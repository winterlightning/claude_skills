"""Plate of Round Dumplings.
Symbol plan: Three overlapping round dumplings over shallow plate. Bounds (4,8)-(44,40).
Construction reference: Supplied round dumpling mound; Lucide soup broad serving rim.
Reduction: Four dumplings reduced to three clear overlapping lobes; double plate rim omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8be028bd-19dc-458e-b618-869a78d5e4dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/naan dish_8be028bd-19dc-458e-b618-869a78d5e4dc.svg'
AUTHOR = 'gpt-6'

class RoundDumplingPlate(Solo48):
    icon_id = 'round-dumpling-plate'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('round', 'dumpling', 'plate')

    def build(self):
        for n,x in [('left',15),('right',33)]:
         self.add_arc(n+'-a',(x-9,28),(x,19),radius_x=9);self.add_arc(n+'-b',(x,19),(x+9,28),radius_x=9);self.add_contour(n,n+'-a',n+'-b')
        self.relate('connect','left','right')
        self.add_arc('back',(15,19),(33,19),radius_x=9,radius_y=11)
        for n in ('left','right'):self.relate('connect','back',n)
        self.add_polyline('front',(6,28),(24,28),(42,28))
        for n in ('left','right'):self.relate('connect','front',n)
        self.path('plate',(6,28),[(4,28),((4,35),(12,40),(24,40)),((36,40),(44,35),(44,28)),(42,28)]);self.relate('connect','plate','front')
        for n in ('left','right'):self.relate('connect','plate',n)

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
