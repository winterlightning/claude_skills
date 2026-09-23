"""crop rotate. Reconstructed whole reference on SOLO48.
Plan: SQUARE visible bounds (4, 4, 44, 44).
Construction: crop and rotate-ccw. Shared dimensions and relationships are recorded in build.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b05e7a98-e0c7-5855-a771-4dc4b12ff639'
SOURCE_PATH = 'icon_set/work/todo-references/crop rotate_b05e7a98-e0c7-5855-a771-4dc4b12ff639.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crop-rotate'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('crop', 'rotate')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def rounded_rect(self, name, x, y, w, h, r):
        nodes=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=nodes[i],nodes[(i+1)%8];eid=f'{name}-{i}';members.append(eid)
            if i%2:self.add_arc(eid,a,b,radius_x=r)
            else:self.add_line(eid,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Two opposing crop corners and two quarter-turn arrows.
        self.add_polyline('crop-left',(14,6),(14,34),(42,34))
        self.add_polyline('crop-right',(6,14),(34,14),(34,42))
        # Actual crop strokes intersect at the original intended crossing points.
        self.relate('connect','crop-left','crop-right')
        self.add_arc('rotate-top',(42,22),(30,10),radius_x=12,sweep=False)
        self.add_polyline('arrow-top',(34,6),(30,10),(34,12))
        self.relate('connect','rotate-top','arrow-top')
        self.add_arc('rotate-bottom',(6,26),(18,38),radius_x=12,sweep=False)
        self.add_polyline('arrow-bottom',(12,34),(18,38),(14,42))
        self.relate('connect','rotate-bottom','arrow-bottom')

