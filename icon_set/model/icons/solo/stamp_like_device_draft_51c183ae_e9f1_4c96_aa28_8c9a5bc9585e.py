'Manual Rubber Stamp.\nPlan: Preserve the ambiguous incomplete stamp-like outline: top grip, stem, tapered body and open long lower-right edge. Bounds8,4..40,44.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: User explicitly requested preservation as an ambiguous draft; do not invent a lower boundary or identify it as a completed stamp/POS device.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51c183ae-e9f1-4c96-aa28-8c9a5bc9585e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/POS machine_51c183ae-e9f1-4c96-aa28-8c9a5bc9585e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stamp-like-device-draft'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('stamp', 'like', 'device', 'draft')

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

        self.add_line('grip',(16,4),(32,4));self.add_line('stem',(24,4),(24,14));self.relate('connect','grip','stem')
        self.add_polyline('upper',(12,24),(16,14),(32,14),(36,24));self.relate('connect','stem','upper')
        self.add_polyline('base',(8,24),(40,24),(40,44));self.relate('connect','upper','base')
