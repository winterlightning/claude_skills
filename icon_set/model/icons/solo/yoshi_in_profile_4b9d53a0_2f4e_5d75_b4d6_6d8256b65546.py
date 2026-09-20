'Yoshi Dinosaur Character Icon.\nPlan: Right-facing dinosaur with raised head lobe, large snout, left tail and broad foot. Eye, arm and saddle seam omitted for clearance. Bounds6..42.\nReference: No useful local Lucide Yoshi match; original character silhouette with coherent circular lobes.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b9d53a0-2f4e-5d75-b4d6-6d8256b65546'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-07/mario yoshi_4b9d53a0-2f4e-5d75-b4d6-6d8256b65546.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'yoshi-in-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('yoshi', 'in', 'profile')

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

        path('yoshi',(20,12),[(20,10),((28,10),4,4,True),(34,10),((42,18),8,8,True),((34,26),8,8,True),(28,24),(26,32),(34,42),(18,42),(18,36),((6,24),12,12,True),(18,28),(20,22),(20,12)],True)
