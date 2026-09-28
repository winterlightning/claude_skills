"""Professional Chef Hat.
Symbol plan: Three-lobed crown and tall body with rounded lower band. Bounds (8,4)-(40,44).
Construction reference: Supplied tall rounded toque; Lucide chef-hat three crown lobes and lower band.
Reduction: No extra fabric folds; rounded base distinguishes this source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29a7e9d8-9673-580c-97d8-21e2a55c1df6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear asian hat_29a7e9d8-9673-580c-97d8-21e2a55c1df6.svg'
AUTHOR = 'gpt-6'

class ProfessionalChefHatRounded(Solo48):
    icon_id = 'professional-chef-hat-rounded'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('professional', 'chef', 'hat', 'rounded')

    def build(self):
        axis=24
        self.path('hat',(axis,4),[((19,4),(16,7),(16,10)),((10,8),(8,12),(8,16)),((8,22),(10,24),(14,24)),(14,35),(14,40),((14,43),(16,44),(18,44)),(30,44),((32,44),(34,43),(34,40)),(34,35),(34,24),((38,24),(40,22),(40,16)),((40,12),(38,8),(32,10)),((32,7),(29,4),(axis,4))],True)
        self.add_line('band',(14,35),(34,35));self.relate('connect','band','hat')

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
