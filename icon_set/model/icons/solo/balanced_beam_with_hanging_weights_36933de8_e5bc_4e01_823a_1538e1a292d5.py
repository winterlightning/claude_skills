'Balanced Weight Scales.\nPlan: Balanced beam suspends two equal round weights above a central pedestal. Both weights share size and height.\nReference: Lucide scale: symmetric beam and central upright; source circular weights retained.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36933de8-e5bc-4e01-823a-1538e1a292d5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_21/h1_36933de8-e5bc-4e01-823a-1538e1a292d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'balanced-beam-with-hanging-weights'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('balanced', 'beam', 'with', 'hanging', 'weights')

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

        self.add_polyline('beam',(9,18),(9,8),(24,8),(39,8),(39,18))
        for j,x in enumerate((9,39)):circle(f'weight-{j}',x,23,5);self.relate('connect',f'weight-{j}','beam')
        self.add_line('upright',(24,8),(24,32));self.relate('connect','upright','beam');box('base',16,32,32,40,4);self.relate('connect','base','upright')
