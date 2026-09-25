"""Pattypan Summer Squash.
Symbol plan: Scalloped broad shoulder and paired sweeping ribs; center24. Bounds (4,8)-(44,40).
Construction reference: Supplied pattypan; no direct useful Lucide match.
Reduction: Small central crease omitted; broad shoulder and two ribs retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ec5c497-854f-419d-8975-c7e41a655bfd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/patty pan squash_4ec5c497-854f-419d-8975-c7e41a655bfd.svg'
AUTHOR = 'gpt-6'

class PattypanSummerSquash(Solo48):
    icon_id = 'pattypan-summer-squash'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('pattypan', 'summer', 'squash')

    def build(self):
        axis=24
        self.path('body',(4,22),[((4,16),(10,14),(14,16)),((18,12),(20,14),(axis,16)),((28,14),(30,12),(34,16)),((38,14),(44,16),(44,22)),((44,30),(34,40),(axis,40)),((14,40),(4,30),(4,22))],True)
        for j,mirror in enumerate((False,True)):
         def p(x,y):return (2*axis-x if mirror else x,y)
         self.add_bezier('rib-'+str(j),p(14,16),(p(14,30),p(18,36),p(24,40)));self.relate('connect','rib-'+str(j),'body')
        self.relate('connect','rib-0','rib-1')
        self.add_line('stem',(axis,8),(axis,16));self.relate('connect','stem','body')

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
