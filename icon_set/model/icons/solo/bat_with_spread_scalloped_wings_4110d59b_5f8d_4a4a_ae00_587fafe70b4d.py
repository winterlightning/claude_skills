'Flying Halloween Bat.\nPlan: A broad bat silhouette uses mirrored swept wings, a small central head and scalloped lower wing edges. Facial details omitted.\nReference: No useful local Lucide bat match; symmetric source silhouette built from shared wing curves.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4110d59b-5f8d-4a4a-ae00-587fafe70b4d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_21/halloween bat fly_4110d59b-5f8d-4a4a-ae00-587fafe70b4d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bat-with-spread-scalloped-wings'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('bat', 'with', 'spread', 'scalloped', 'wings')

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

        path('bat',(4,8),[(18,16),(20,12),(28,12),(30,16),(44,8),((40,32),4,24,True),((32,28),8,4,False),((24,40),8,12,False),((16,28),8,12,False),((8,32),8,4,False),((4,8),4,24,True)],True)
