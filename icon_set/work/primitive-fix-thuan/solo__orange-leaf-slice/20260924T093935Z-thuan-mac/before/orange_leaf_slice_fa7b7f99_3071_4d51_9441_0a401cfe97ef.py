"""Orange Fruit with Leaf and Slice.
Symbol plan: Whole orange behind diagonal cut wedge with attached upper-left leaf. Bounds (6,6)-(42,42).
Construction reference: Supplied orange and wedge; Lucide citrus segment and curved rind construction.
Reduction: Double rind omitted; short stem, leaf and one segment division retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa7b7f99-3071-4d51-9441-0a401cfe97ef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/orange grapefruit citrus_fa7b7f99-3071-4d51-9441-0a401cfe97ef.svg'
AUTHOR = 'gpt-6'

class OrangeLeafSlice(Solo48):
    icon_id = 'orange-leaf-slice'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('orange', 'leaf', 'slice')

    def build(self):
        self.path('whole',(30,26),[((28,25),(26,25),(24,25)),((14,25),(6,25),(6,34)),((6,38),(10,41),(14,42))])
        self.path('slice',(14,42),[(28,28),(30,26),(42,14),((42,26),(38,34),(34,38)),((30,41),(23,42),(14,42))],True);self.relate('connect','whole','slice')
        self.path('leaf',(24,16),[((15,19),(8,14),(6,6)),((15,6),(24,8),(24,16))],True)
        self.add_line('stem',(24,16),(24,25));self.relate('connect','stem','whole');self.relate('connect','stem','leaf')
        self.add_line('segment',(28,28),(34,38));self.relate('connect','segment','slice')

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
