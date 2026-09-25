'Rabbit Head Animal Icon.\nPlan: Two long rounded ears and a broad cheek contour, without facial marks. Symmetric x24; bounds8,4..40,44.\nReference: Lucide rabbit: elongated ears and rounded animal contours; frontal source silhouette retained.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4cefe28-f308-4a73-a992-65a60c997032'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_19/food allegic vegan meal rabbit_b4cefe28-f308-4a73-a992-65a60c997032.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rabbit-head-silhouette'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('rabbit', 'head', 'silhouette')

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

        path('rabbit',(8,32),[(12,22),(8,10),((18,10),5,6,True),(20,20),(28,20),(30,10),((40,10),5,6,True),(36,22),(40,32),((8,32),16,12,True)],True)
