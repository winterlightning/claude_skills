'Three Dimensional Cube Shape.\nPlan: Three-quarter cube with a diamond top, two sides and a shared central vertical edge.\nConstruction reference: Lucide box: three faces constructed around shared corner nodes.\nReduction: Tiny corner rounding reduced to crisp deliberate cube edges.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a4b012b-1c60-486d-9f80-a3a9af239ca7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/sugar_0a4b012b-1c60-486d-9f80-a3a9af239ca7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-edge-solid-cube'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('rounded', 'edge', 'solid', 'cube')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        self.add_polyline('outline',(24,4),(40,12),(40,36),(24,44),(8,36),(8,12),closed=True)
        self.add_polyline('top',(8,12),(24,20),(40,12));self.relate('connect','top','outline')
        self.add_line('edge',(24,20),(24,44));self.relate('connect','edge','top');self.relate('connect','edge','outline')
