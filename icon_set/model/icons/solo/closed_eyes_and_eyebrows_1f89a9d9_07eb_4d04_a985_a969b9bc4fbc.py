'Closed Eyes and Eyebrows.\nPlan: Mirrored arching brows over two closed eyelids. Four coherent curves; bounds4,10..44,38.\nReference: Lucide eye-closed: sweeping eyelid curves; source face detail has no surrounding head.\nKeyshape: HRECT_M, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f89a9d9-07eb-4d04-a985-a969b9bc4fbc'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/eyebrows_1f89a9d9-07eb-4d04-a985-a969b9bc4fbc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-eyes-and-eyebrows'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('closed', 'eyes', 'and', 'eyebrows')

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

        for j,(l,r) in enumerate(((4,18),(30,44))):path(f'brow-{j}',(l,16),[((r,16),7,6,True)])
        for j,(l,r) in enumerate(((6,16),(32,42))):path(f'lid-{j}',(l,32),[((r,32),5,6,False)])
