'Vertical Height Indicator.\nPlan: Two horizontal bounds at6/42 and central double arrow from14 to34. Shared shaft endpoints and mirrored heads.\nReference: No useful Lucide exact subject match; coherent dimension diagram from source, no lettering.\nKeyshape: SQUARE; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6d42fab-1696-4687-b245-2cc151e4cba1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/text height_d6d42fab-1696-4687-b245-2cc151e4cba1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vertical-height-indicator'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('vertical', 'height', 'indicator')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
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

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        for j,y in enumerate((6,42)):self.add_line(f'limit-{j}',(6,y),(42,y))
        self.add_line('shaft',(24,14),(24,34))
        for j,(tip,side) in enumerate(((14,20),(34,28))):
         self.add_polyline(f'head-{j}',(18,side),(24,tip),(30,side));self.relate('connect','shaft',f'head-{j}')
