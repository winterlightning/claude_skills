"""Papaya Slice with Seeds.
Symbol plan: Elongated asymmetric papaya half with three central seeds. Bounds (8,4)-(40,44).
Construction reference: Supplied papaya; Lucide bean for organic tapered outline.
Reduction: Inner cavity outline omitted to preserve clear seeds and a broad flesh band at 48 pixels.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dce3a197-6cbe-46f3-9f0d-900eb67b74fb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/papaya slice_dce3a197-6cbe-46f3-9f0d-900eb67b74fb.svg'
AUTHOR = 'gpt-6'

class PapayaSliceSeeds(Solo48):
    icon_id = 'papaya-slice-seeds'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('papaya', 'slice', 'seeds')

    def build(self):
        self.path('fruit',(28,4),[((37,4),(40,10),(40,18)),((40,25),(35,29),(32,38)),((30,44),(22,44),(18,44)),((10,44),(8,40),(8,32)),((8,20),(18,15),(21,9)),((23,6),(25,4),(28,4))],True)
        for j,p in enumerate([(27,16),(24,25),(19,34)]):self.add_dot('seed-'+str(j),p)

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
