'Giant Person Next to House.\nPlan: Tall stick figure and small house share ground. Head radius5 at14,11; torso starts14,24, exact4 ink gap along vertical torso axis. Straight arms at24 avoid crowding legs. Omit tiny doorway.\nReference: human_ref/full_body_ref.png: circular head and coherent torso/limbs, head axis vertical and exact4 ink gap. House emphasizes scale.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dc2c18c-43e0-46cc-a8a2-8e6ad511487a'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-03/fantasy giant_8dc2c18c-43e0-46cc-a8a2-8e6ad511487a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'giant-beside-house'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('giant', 'beside', 'house')

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

        circle('head',14,11,5)
        self.add_line('torso',(14,24),(14,32))
        self.add_polyline('arms',(6,24),(14,24),(22,24));self.relate('connect','arms','torso')
        self.add_polyline('legs',(8,42),(14,32),(20,42));self.relate('connect','legs','torso')
        self.add_polyline('house',(30,42),(30,34),(36,28),(42,34),(42,42))
        self.add_polyline('ground',(6,42),(8,42),(20,42),(30,42),(42,42));self.relate('connect','ground','legs');self.relate('connect','ground','house')
        self.mark_human_figure('giant',head='head',torso='torso',torso_junction='start')
