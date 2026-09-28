"""cog dollar: complete reference reconstructed on SOLO48.
Keyshape: SQUARE, visible bounds (4, 4, 44, 44).
Construction reference: settings and circle-dollar-sign. See build comments for symbols and relationships.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fa84ff77-a565-4df3-9360-0b7e9c3de772'
SOURCE_PATH = 'icon_set/work/todo-references/cog dollar_fa84ff77-a565-4df3-9360-0b7e9c3de772.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cog-dollar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('cog', 'dollar')

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
        # Eight teeth derive from one quarter; paired dimensions stay equal.
        quarter=[(-4,-18),(4,-18),(4,-16),(9,-14),(12,-16),(16,-12),(14,-9),(16,-4)]
        pts=[]
        for turn in range(4):
            for x,y in quarter:
                for _ in range(turn):x,y=-y,x
                pts.append((24+x,24+y))
        self.add_polyline('gear',*pts,closed=True)
        # S bowl is split at shared endpoints for the two exposed currency stems.
        self.add_arc('s-top',(28,18),(24,17),radius_x=8)
        self.add_arc('s-upper',(24,17),(24,24),radius_x=6,radius_y=5,sweep=False)
        self.add_arc('s-lower',(24,24),(24,31),radius_x=6,radius_y=5)
        self.add_arc('s-bottom',(24,31),(20,30),radius_x=8)
        self.add_contour('s','s-top','s-upper','s-lower','s-bottom')
        self.add_line('stem-top',(24,15),(24,17))
        self.add_line('stem-bottom',(24,31),(24,33))
        self.relate('connect','s','stem-top')
        self.relate('connect','s','stem-bottom')

