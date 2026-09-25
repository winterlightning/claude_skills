'Simple Home Icon.\n\nSymbol plan: A single completed plain house silhouette with pitched roof and no added openings. Shared vertical axis x24; extremes (6,6)-(42,42).\nConstruction reference: Lucide house: one connected facade silhouette, preserving empty source facade.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec2ee580-8299-48ed-a4a0-a9671a77bb79'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/valley_ec2ee580-8299-48ed-a4a0-a9671a77bb79.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'simple-house'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('simple', 'house')

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

        self.add_polyline('house',(6,24),(24,6),(42,24),(42,42),(6,42),closed=True)
