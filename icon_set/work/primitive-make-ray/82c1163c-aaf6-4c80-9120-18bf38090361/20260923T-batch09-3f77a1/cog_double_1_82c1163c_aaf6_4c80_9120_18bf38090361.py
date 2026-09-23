"""cog double 1: complete reference reconstructed on SOLO48.
Keyshape: SQUARE, visible bounds (4, 4, 44, 44).
Construction reference: settings. See build comments for symbols and relationships.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '82c1163c-aaf6-4c80-9120-18bf38090361'
SOURCE_PATH = 'icon_set/work/todo-references/cog double 1_82c1163c-aaf6-4c80-9120-18bf38090361.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cog-double-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('cog', 'double', '1')

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
        # Two equal eight-toothed gears sit on the rising diagonal.
        # Each quarter shares the same tooth and root offsets; centres are independent.
        quarter=[(-2,-10),(2,-10),(2,-8),(5,-7),(7,-8),(8,-7),(7,-5),(8,-2)]
        for i,(cx,cy) in enumerate(((16,32),(32,16))):
            pts=[]
            for turn in range(4):
                for x,y in quarter:
                    for _ in range(turn):x,y=-y,x
                    pts.append((cx+x,cy+y))
            self.add_polyline(f'gear-{i}',*pts,closed=True)
            self.circle(f'hub-{i}',cx,cy,4)

