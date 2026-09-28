"""Pizza with Separated Slice.
Symbol plan: Round pizza missing upper-right quarter, detached quarter above gap and three toppings. Bounds (6,6)-(42,42).
Construction reference: Supplied separated pizza; Lucide pizza sector geometry.
Reduction: Double crust bands omitted; three toppings and detached slice preserved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4e7d790-c116-400e-a0bd-daaa28f39eae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pizza_b4e7d790-c116-400e-a0bd-daaa28f39eae.svg'
AUTHOR = 'gpt-6'

class PizzaSeparatedSlice(Solo48):
    icon_id = 'pizza-separated-slice'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('pizza', 'separated', 'slice')

    def build(self):
        self.add_arc('whole-lower',(42,24),(6,24),radius_x=18)
        self.add_arc('whole-upper',(6,24),(24,6),radius_x=18)
        self.add_line('cut-top',(24,6),(24,24));self.add_line('cut-right',(24,24),(42,24));self.add_contour('pizza','whole-lower','whole-upper','cut-top','cut-right',closed=True)
        self.add_arc('slice-rim',(33,6),(42,15),radius_x=9)
        self.add_polyline('slice-cut',(42,15),(33,15),(33,6));self.relate('connect','slice-rim','slice-cut')
        for j,p in enumerate([(15,22),(17,31),(26,33)]):self.add_dot('topping-'+str(j),p)

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
