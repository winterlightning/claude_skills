'Adjustable Suspenders Straps.\nPlan: Two identical straps at shared y limits; buckle is a broad horizontal divider.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Each buckle reduced to a single crossbar within the strap, retaining the adjustable pair.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '403d3b09-28f3-4968-b55e-9f29cb36fbe9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/suspenders_403d3b09-28f3-4968-b55e-9f29cb36fbe9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-adjustable-suspender-straps'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('paired', 'adjustable', 'suspender', 'straps')

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

        for j,left in enumerate((6,30)):
         right=left+12
         path(f'strap-{j}',(left+4,6),[(right-4,6),((right,10),4,4,True),(right,28),(right,38),((right-4,42),4,4,True),(left+4,42),((left,38),4,4,True),(left,28),(left,10),((left+4,6),4,4,True)],True)
         self.add_line(f'buckle-{j}',(left,28),(right,28));self.relate('connect',f'buckle-{j}',f'strap-{j}')
