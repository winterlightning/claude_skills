'Wrench and Screwdriver Tools.\nPlan: Parallel diagonal wrench and complete screwdriver with open wrench jaw. Bounds6..42.\nConstruction reference: Lucide wrench original/atomic-debug open jaw and long grip; source parallel tools layout.\nReduction: Simplify grip rounding and omit screwdriver grooves.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '774bfcef-0999-44e7-9307-b99279f04ee1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tool organizer 1_774bfcef-0999-44e7-9307-b99279f04ee1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wrench-and-screwdriver'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('wrench', 'and', 'screwdriver')

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

        self.add_polyline('wrench',(6,30),(16,18),(16,10),(24,6),(24,14),(32,14),(26,22),(12,36),(6,36),closed=True)
        self.add_polyline('handle',(24,36),(34,26),(40,32),(30,42),closed=True)
        self.add_line('shaft',(37,29),(42,24));self.relate('connect','handle','shaft')
