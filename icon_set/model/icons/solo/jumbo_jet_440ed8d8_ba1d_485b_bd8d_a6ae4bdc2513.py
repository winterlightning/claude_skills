'Flying Passenger Airplane.\n\nSymbol plan: One broad diagonal airplane silhouette integrates nose, swept wings and tail. Narrow wing and tail bands widened in the final model to preserve spacing; windows omitted.\nConstruction reference: Lucide plane: coherent integrated wing/fuselage contour with deliberate diagonal orientation.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '440ed8d8-ba1d-485b-bd8d-a6ae4bdc2513'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/jumbo jet_440ed8d8-ba1d-485b-bd8d-a6ae4bdc2513.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'jumbo-jet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('jumbo', 'jet')

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

        path('plane',(36,6),[((42,12),6,6,True),(32,22),(40,38),(32,42),(24,30),(16,38),(6,42),(6,32),(14,24),(6,16),(6,8),(24,16),(36,6)],True)
