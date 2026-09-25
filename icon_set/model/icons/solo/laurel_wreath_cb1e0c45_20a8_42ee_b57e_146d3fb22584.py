'Victory Laurel Wreath.\nPlan: Open laurel wreath formed by two pairs of pointed broad leaves and crossed bare stems. Bounds6..42.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Reduce numerous leaves to two broad pointed leaves per branch, preserving an open wreath and crossed stems.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb1e0c45-20a8-42ee-b57e-146d3fb22584'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/laurel wreath_cb1e0c45-20a8-42ee-b57e-146d3fb22584.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'laurel-wreath'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('laurel', 'wreath')

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

        for side in (-1,1):
         def p(x,y):return (24+side*(x-24),y)
         self.add_bezier(f'upper-{side}',p(14,6),(p(8,6),p(6,10),p(6,15)),(p(6,20),p(8,24),p(14,24)),(p(18,22),p(18,20),p(18,15)),(p(18,10),p(18,8),p(14,6)))
         self.add_bezier(f'lower-{side}',p(14,24),(p(10,22),p(6,22),p(6,24)),(p(6,32),p(12,34),p(18,34)),(p(20,30),p(18,26),p(14,24)))
         self.add_line(f'stem-{side}',p(18,34),p(26,42))
         self.relate('connect',f'upper-{side}',f'lower-{side}');self.relate('connect',f'lower-{side}',f'stem-{side}')
        self.relate('connect','stem--1','stem-1')
