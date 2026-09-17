"""Open Pea Pod with Peas.
Symbol plan: Curving open pod and three seed dots. Bounds (4,8)-(44,40).
Construction reference: Supplied open pea pod; Lucide bean smooth silhouette.
Reduction: Pea outlines reduced to three dots; lower pod scallops retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '772eace8-9c23-413a-b80c-9156dbf20f6a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pea_772eace8-9c23-413a-b80c-9156dbf20f6a.svg'
AUTHOR = 'gpt-6'

class OpenPeaPod(Solo48):
    icon_id = 'open-pea-pod'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('open', 'pea', 'pod')

    def build(self):
        self.path('pod',(4,30),[((4,8),(33,10),(44,8)),((44,22),(42,30),(34,34)),((31,39),(26,40),(22,37)),((19,39),(16,40),(13,40)),((8,40),(4,38),(4,34)),(4,30)],True)
        for j,p in enumerate([(14,26),(25,24),(35,19)]):self.add_dot('pea-'+str(j),p)

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
