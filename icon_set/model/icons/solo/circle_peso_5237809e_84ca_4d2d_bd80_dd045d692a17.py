"""circle peso: complete reference reconstructed on SOLO48.
Keyshape: CIRCLE, visible bounds (2, 2, 46, 46).
Construction reference: circle-dollar-sign. See build comments for symbols and relationships.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5237809e-84ca-4d2d-bd80-dd045d692a17'
SOURCE_PATH = 'icon_set/work/todo-references/circle peso_5237809e-84ca-4d2d-bd80-dd045d692a17.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-peso'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('circle', 'peso')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def rounded_rect(self, name, x, y, w, h, r):
        nodes=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=nodes[i],nodes[(i+1)%8]; eid=f'{name}-{i}';members.append(eid)
            if i%2:self.add_arc(eid,a,b,radius_x=r)
            else:self.add_line(eid,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        self.circle('ring',24,24,20)
        # P bowl and single peso crossbar; a shared baseline anchors the symbol.
        self.add_polyline('stem',(18,34),(18,14),(25,14))
        self.add_arc('bowl',(25,14),(25,24),radius_x=5)
        self.add_polyline('crossbar',(14,24),(18,24),(25,24))
        self.relate('connect','stem','bowl')
        self.relate('connect','stem','crossbar')
        self.relate('connect','bowl','crossbar')

