'Pundi X Cryptocurrency Logo.\nSymbol plan: Two mirrored diagonals with a wide bottom gap. Endpoints(4,10)/(18,38), mirrored around24. No connected central point.\nConstruction reference: No useful Lucide subject match; two exact mirrored straight strokes.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68ed9edc-eb14-49f0-aa97-179f9ae7f501'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/virtual coin crypto pundi x_68ed9edc-eb14-49f0-aa97-179f9ae7f501.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'pundi-x-separated-diagonals'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pundi', 'x', 'separated', 'diagonals')

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

        for sign in (-1,1): self.add_line(f'stroke-{sign}',(24+sign*20,10),(24+sign*6,38))
