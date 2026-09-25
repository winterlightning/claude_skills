"""Mooncake Slice with Egg Yolk.
Symbol plan: Scalloped top and thick rectangular cut face with half-round yolk. Bounds (4,8)-(44,40).
Construction reference: Supplied mooncake cut; Lucide citrus separated cut-surface bands.
Reduction: Top stamp and dense scallops omitted; yolk and crust retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '12342eb1-01c0-4970-94e4-8869bddbadcd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mooncake slice_12342eb1-01c0-4970-94e4-8869bddbadcd.svg'
AUTHOR = 'gpt-6'

class MooncakeSliceEggYolk(Solo48):
    icon_id = 'mooncake-slice-egg-yolk'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('mooncake', 'slice', 'egg', 'yolk')

    def build(self):
        self.path('face',(4,22),[(44,22),(44,40),(33,40),(15,40),(4,40),(4,22)],True)
        self.path('crust',(4,22),[((4,14),(8,12),(14,12)),((14,8),(18,8),(24,8)),((30,8),(33,10),(34,12)),((40,12),(44,16),(44,22))]);self.relate('connect','crust','face')
        self.add_arc('yolk',(15,40),(33,40),radius_x=9);self.relate('connect','yolk','face')

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
