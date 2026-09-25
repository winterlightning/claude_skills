'Windy Weather Cloud.\nPlan: Three-lobed cloud with two separated wind strokes at33 and42. Cloud top6/bottom24, x6..42. Omit source outline break, retain two wind lines.\nReference: No cloud-wind Lucide match; smooth lobe principles from cloud construction; horizontal wind strokes retain source meaning.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35540408-430e-454b-92bd-2db38fb57d88'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/weather cloud wind 2_35540408-430e-454b-92bd-2db38fb57d88.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloud-with-wind-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cloud', 'with', 'wind', 'lines')

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

        path('cloud',(14,24),[((6,16),8,8,True),((16,10),10,6,True),((32,10),8,4,True),((42,16),10,6,True),((34,24),8,8,True),(14,24)],True)
        self.add_line('wind-upper',(8,33),(30,33))
        self.add_line('wind-lower',(8,42),(22,42))
