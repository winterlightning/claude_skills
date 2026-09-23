"""An empty eight-point award badge with stepped shoulders.
Plan: One closed badge contour; four identical quarter-turn groups around the shared center.
Construction reference: badge: repeated radial symmetry; retain the supplied angular shoulders rather than circular scallops.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '83414ae1-83ad-4f09-a7d9-9c6c5864840a'
SOURCE_PATH = 'icon_set/work/todo-references/badge 1_83414ae1-83ad-4f09-a7d9-9c6c5864840a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'badge-1'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('badge', '1')
    # Bounds are supplied by the contract; geometry below is authored to them.
    planned_visible_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, left, top, right, bottom, radius=4):
        r = radius
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members = []
        for i, start in enumerate(points):
            end = points[(i+1)%8]
            part = f'{name}-{i}'
            if i%2:
                self.add_arc(part,start,end,radius_x=r)
            else:
                self.add_line(part,start,end)
            members.append(part)
        self.add_contour(name,*members,closed=True)

    def build(self):
        axis = 24
        quarter = [(0,-18),(6,-12),(12,-12),(12,-6)]
        points=[]
        for turn in range(4):
            for x,y in quarter:
                for _ in range(turn):
                    x,y=-y,x
                points.append((axis+x,axis+y))
        self.add_polyline('badge',*points,closed=True)
