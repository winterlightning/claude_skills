'Toothpaste Tube Container.\nPlan: Upright tube with short cap, shoulder seam and sealed base.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Shoulder seam omitted, leaving the cap join and bottom seal.\nKeyshape: VRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38751771-5fa5-4ce3-8486-0d1b5bd54bd5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/toothpaste_38751771-5fa5-4ce3-8486-0d1b5bd54bd5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toothpaste-tube'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('toothpaste', 'tube')

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

        path('body',(18,12),[(30,12),((34,18),4,6,True),(38,44),(10,44),(14,18),((18,12),4,6,True)],True)
        self.add_polyline('cap',(18,12),(18,4),(30,4),(30,12));self.relate('connect','cap','body')
        self.add_line('seal',(11,36),(37,36));self.relate('connect','seal','body')
