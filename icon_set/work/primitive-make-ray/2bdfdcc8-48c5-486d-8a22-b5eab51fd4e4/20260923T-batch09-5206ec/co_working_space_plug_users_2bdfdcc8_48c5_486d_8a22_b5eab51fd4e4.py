"""co working space plug users: complete reference reconstructed on SOLO48.
Keyshape: SQUARE, visible bounds (4, 4, 44, 44).
Construction reference: human_ref/user.svg and plug. See build comments for symbols and relationships.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2bdfdcc8-48c5-486d-8a22-b5eab51fd4e4'
SOURCE_PATH = 'icon_set/work/todo-references/co working space plug users_2bdfdcc8-48c5-486d-8a22-b5eab51fd4e4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'co-working-space-plug-users'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('co', 'working', 'space', 'plug', 'users')

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
        # Two equivalent user busts below a continuous cord and disconnected plug.
        # Human reference: icon_set/references/human_ref/user.svg.
        # Each head bottom = 32; shoulder top = 40: exact 8 centreline / 4 ink gap.
        for i,cx in enumerate((13,35)):
            self.circle(f'head-{i}',cx,28,4)
            self.add_arc(f'shoulders-{i}',(cx-7,42),(cx+7,42),radius_x=7,radius_y=2)
        self.add_polyline('cord',(14,12),(6,12),(6,24),(42,24),(42,12),(36,12))
        self.rounded_rect('plug',12,6,8,14,3)
        self.rounded_rect('socket',30,6,8,14,3)
        for j,y in enumerate((8,16)):
            self.add_line(f'pin-{j}',(20,y),(24,y))
            self.relate('connect','plug',f'pin-{j}')
            self.add_dot(f'socket-hole-{j}',(34,y))
        self.relate('connect','cord','plug')
        self.relate('connect','cord','socket')

