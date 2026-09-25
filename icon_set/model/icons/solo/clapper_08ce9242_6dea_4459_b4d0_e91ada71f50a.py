"""clapper: complete reference reconstructed on SOLO48.
Keyshape: HRECT_L, visible bounds (2, 6, 46, 42).
Construction reference: clapperboard. See build comments for symbols and relationships.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '08ce9242-6dea-4459-b4d0-e91ada71f50a'
SOURCE_PATH = 'icon_set/work/todo-references/clapper_08ce9242-6dea-4459-b4d0-e91ada71f50a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clapper'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('clapper',)

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
        # Closed clapperboard: rounded body, header seam and diagonal slate mark.
        self.rounded_rect('board',4,8,40,32,4)
        self.add_line('seam',(4,20),(44,20))
        self.add_line('stripe',(12,20),(24,8))
        self.relate('connect','board','seam')
        self.relate('connect','board','stripe')
        self.relate('connect','seam','stripe')
        self.add_line('label',(13,30),(35,30))

