"""Kitchen Baking Oven Appliance.
Symbol plan: Rounded oven body; regular control row and lower window. Bounds (6,6)-(42,42).
Construction reference: Supplied oven; Lucide microwave rounded case and inset window.
Reduction: Panel seam omitted; knobs reduced to distinct dots.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ebfc23c-058f-4089-adb1-309ca3bb6e6f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/oven_2ebfc23c-058f-4089-adb1-309ca3bb6e6f.svg'
AUTHOR = 'gpt-6'

class KitchenBakingOven(Solo48):
    icon_id = 'kitchen-baking-oven'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('kitchen', 'baking', 'oven')

    def build(self):
        l,r,t,b=6,42,6,42
        self.path('body',(l+4,t),[(r-4,t),((r,t),(r,t),(r,t+4)),(r,b-4),((r,b),(r,b),(r-4,b)),(l+4,b),((l,b),(l,b),(l,b-4)),(l,t+4),((l,t),(l,t),(l+4,t))],True)
        for j,x in enumerate((15, 24, 33)):self.add_dot('control-'+str(j),(x,15))
        l,t,r,b=(15, 24, 33, 33)
        self.path('window',(l+2,t),[(r-2,t),((r,t),(r,t),(r,t+2)),(r,b-2),((r,b),(r,b),(r-2,b)),(l+2,b),((l,b),(l,b),(l,b-2)),(l,t+2),((l,t),(l,t),(l+2,t))],True)

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
