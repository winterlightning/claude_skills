'Glass Bottle with Label.\nPlan: Squat bottle with narrow neck and broad label band. Shared cap and label seams; symmetric x24. Bounds10,4..38,44.\nReference: Lucide bottle-wine: rounded shoulders and shared bottle label boundaries.\nKeyshape: VRECT_M, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5da482e1-3c65-49ae-9b42-cd72cfb09489'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/whiskey_5da482e1-3c65-49ae-9b42-cd72cfb09489.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'labeled-bottle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('labeled', 'bottle')

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

        path('bottle',(20,4),[(28,4),(28,12),((38,22),10,10,True),(38,24),(38,34),(38,40),((34,44),4,4,True),(14,44),((10,40),4,4,True),(10,34),(10,24),(10,22),((20,12),10,10,True),(20,4)],True)
        for y in (24,34):self.add_line(f'label-{y}',(10,y),(38,y));self.relate('connect',f'label-{y}','bottle')
        self.add_line('cap',(20,12),(28,12));self.relate('connect','cap','bottle')
