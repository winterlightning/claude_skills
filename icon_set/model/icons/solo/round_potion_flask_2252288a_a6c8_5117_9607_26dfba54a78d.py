'Round Magic Potion Bottle.\nPlan: Round flask with a flush stopper, narrow neck, circular belly and liquid wave; projecting lip omitted to open shoulder clearance.\nReference: Lucide flask-round: coherent rounded body and shared liquid boundary.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2252288a-a6c8-5117-9607-26dfba54a78d'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-09/potion_2252288a-a6c8-5117-9607-26dfba54a78d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-potion-flask'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    aliases = ()
    keywords = ('round', 'potion', 'flask')

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

        path('bottle',(20,12),[(20,16),((8,28),12,12,False),((24,44),16,16,False),((40,28),16,16,False),((28,16),12,12,False),(28,12)])
        self.add_polyline('lip',(20,12),(28,12));self.relate('connect','lip','bottle')
        self.add_polyline('stopper',(20,12),(20,4),(28,4),(28,12));self.relate('connect','stopper','lip');self.relate('connect','stopper','bottle')
        path('liquid',(8,28),[((24,28),8,2,False),((40,28),8,2,True)]);self.relate('connect','liquid','bottle')
