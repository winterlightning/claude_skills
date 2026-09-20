'Sonic the Hedgehog Head.\nPlan: Left-facing hedgehog head with swept spines, pointed ear, visible eye and curved smile. Fine muzzle partitions omitted.\nReference: No useful local Lucide Sonic match; source distinctive backward spines, ear and projecting nose retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd4af04d-14e9-43e9-b2be-0d5394a02f2e'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-10/sonic_fd4af04d-14e9-43e9-b2be-0d5394a02f2e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sonic-head-three-quarter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sonic', 'head', 'three', 'quarter')

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

        path('sonic',(12,6),[(22,10),(32,6),(40,6),(36,16),(42,20),(36,26),(42,34),(30,38),(24,42),(14,42),((6,34),8,8,True),(6,28),(10,26),(10,18),(12,6)],True)
        self.add_dot('eye',(20,20));path('smile',(18,29),[((26,29),4,2,False)])
