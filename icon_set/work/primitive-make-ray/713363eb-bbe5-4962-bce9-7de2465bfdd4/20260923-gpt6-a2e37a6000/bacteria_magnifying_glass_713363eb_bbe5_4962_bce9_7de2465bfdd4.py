"""A magnifying glass enclosing scattered microbial dots.
Plan: Circular lens owns a diagonal handle attachment and a triangular group of three dots.
Construction reference: search: a circular lens with one attached diagonal handle.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '713363eb-bbe5-4962-bce9-7de2465bfdd4'
SOURCE_PATH = 'icon_set/work/todo-references/bacteria magnifying glass_713363eb-bbe5-4962-bce9-7de2465bfdd4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bacteria-magnifying-glass'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('bacteria', 'magnifying', 'glass')
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
        cx, cy, radius = 21, 21, 15
        join, opposite = (cx+9,cy+12),(cx-9,cy-12)
        self.add_arc('lens-a',join,opposite,radius_x=radius)
        self.add_arc('lens-b',opposite,join,radius_x=radius)
        self.add_contour('lens','lens-a','lens-b',closed=True)
        self.add_line('handle',join,(42,42))
        for arc in ('lens-a','lens-b'):
            self.relate('connect',arc,'handle')
        for i,p in enumerate([(17,17),(25,17),(21,25)]):
            self.add_dot(f'microbe-{i}',p)
