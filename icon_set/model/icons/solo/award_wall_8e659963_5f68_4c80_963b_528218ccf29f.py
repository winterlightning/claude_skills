"""A blank pointed award pennant suspended from a wall rail.
Plan: Upright pennant; shared axis 24 controls the hanger and lower point; rail joins the two side walls.
Construction reference: rectangle-horizontal: a coherent contour with clean corners; preserve the angular pennant tips.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = '8e659963-5f68-4c80-963b-528218ccf29f'
SOURCE_PATH = 'icon_set/work/todo-references/award wall_8e659963-5f68-4c80-963b-528218ccf29f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'award-wall'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ()
    keywords = ('award', 'wall')
    # Bounds are supplied by the contract; geometry below is authored to them.
    planned_visible_bounds = Keyshape.VRECT_L.bounds_for(Profile.SOLO48)

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
        self.add_polyline('hanger',(12,12),(axis,4),(36,12))
        self.add_polyline('pennant',(12,12),(12,34),(axis,44),(36,34),(36,12))
        for i,(a,b) in enumerate([(8,12),(12,36),(36,40)]):
            self.add_line(f'rail-{i}',(a,12),(b,12))
        for rail in ('rail-0','rail-1'):
            self.relate('connect',rail,'hanger-1')
            self.relate('connect',rail,'pennant-1')
        for rail in ('rail-1','rail-2'):
            self.relate('connect',rail,'hanger-2')
            self.relate('connect',rail,'pennant-4')
