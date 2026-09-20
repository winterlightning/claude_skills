'Warm Winter Scarf Accessory.\nPlan: Large scarf neck loop and two separated tails. Bounds8,4..40,44.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Use straight separated tails; omit tiny fringe strokes.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51c04ccd-9615-4a5a-8998-220d4bb707be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stole_51c04ccd-9615-4a5a-8998-220d4bb707be.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'looped-fringed-winter-scarf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('looped', 'fringed', 'winter', 'scarf')

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

        box('loop',8,4,40,24,10)
        self.add_polyline('left-tail',(8,24),(8,44),(20,44),(20,24));self.relate('connect','loop','left-tail')
        self.add_polyline('right-tail',(28,24),(28,44),(40,44),(40,24));self.relate('connect','loop','right-tail')
