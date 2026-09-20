'Handheld Gaming Console Dock.\nPlan: Hand entering from above grips console rim; console partially hidden behind broad docking base. Buttons and tilt reduced for clear overlap. Bounds6..42.\nReference: Lucide hand and gamepad-2: rounded gripping finger and controller corners; human-part reference vocabulary.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb11a30f-fb1c-4930-9aae-280bc7d071fc'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-11/switch dock_fb11a30f-fb1c-4930-9aae-280bc7d071fc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-docking-game-console'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('hand', 'docking', 'game', 'console')

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

        path('hand',(18,6),[(18,14),(18,16),((26,16),4,4,False),(26,14),(26,6)])
        path('console-left',(18,14),[(10,14),((6,18),4,4,False),(6,30),(8,30)])
        path('console-right',(26,14),[(38,14),((42,18),4,4,True),(42,30),(40,30)])
        box('dock',8,30,40,42,4)
        for n in ('console-left','console-right'):self.relate('connect',n,'hand');self.relate('connect',n,'dock')
