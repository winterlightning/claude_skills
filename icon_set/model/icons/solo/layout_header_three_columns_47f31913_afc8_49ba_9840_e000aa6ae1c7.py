'Three Column Web Layout.\nPlan: Rounded interface frame with a header and three equal lower columns.\nConstruction reference: Lucide table: structural dividers within one frame.\nReduction: No omissions; these are layout partitions, not a hosted symbol.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47f31913-afc8-49ba-9840-e000aa6ae1c7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/layout 3_47f31913-afc8-49ba-9840-e000aa6ae1c7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'layout-header-three-columns'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('layout', 'header', 'three', 'columns')

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

        box('frame',6,6,42,42,4)
        self.add_polyline('header',(6,18),(18,18),(30,18),(42,18));self.relate('connect','header','frame')
        for x in (18,30):self.add_line(f'column-{x}',(x,18),(x,42));self.relate('connect',f'column-{x}','frame');self.relate('connect',f'column-{x}','header')
