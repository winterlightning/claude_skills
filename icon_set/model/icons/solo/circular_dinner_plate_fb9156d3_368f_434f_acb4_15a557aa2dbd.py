"""Minimalist Circular Dinner Plate.
Symbol plan: Two concentric circles centered24 with radii20 and11.
Construction reference: Supplied plate; Lucide citrus for concentric circular construction.
Reduction: None; the two-ring silhouette is already minimal.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb9156d3-368f-434f-acb4-15a557aa2dbd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/plate_fb9156d3-368f-434f-acb4-15a557aa2dbd.svg'
AUTHOR = 'gpt-6'

class CircularDinnerPlate(Solo48):
    icon_id = 'circular-dinner-plate'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('circular', 'dinner', 'plate')

    def build(self):
        axis=24
        for name,radius in [('edge',20),('well',11)]:self.loop(name,axis,axis,radius)

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
