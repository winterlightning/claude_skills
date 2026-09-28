'Twisted Braided Rope.\nPlan: Two broad strands twist diagonally around a shared S-shaped seam.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Fine repeated twists consolidated into two broad interwoven strand regions.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f58379fc-9d80-4dda-a9a6-c8a46cd81044'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/twist_f58379fc-9d80-4dda-a9a6-c8a46cd81044.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'twisted-rope'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('twisted', 'rope')

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

        path('rope',(6,34),[((14,26),14,14,True),((24,16),14,14,True),((34,6),14,14,True),((42,14),8,8,True),((32,24),14,14,True),((22,34),14,14,True),((14,42),14,14,True),((6,34),8,8,True)],True)
        path('twist',(14,26),[((23,25),9,4,False),((32,24),9,4,True)]);self.relate('connect','twist','rope')
