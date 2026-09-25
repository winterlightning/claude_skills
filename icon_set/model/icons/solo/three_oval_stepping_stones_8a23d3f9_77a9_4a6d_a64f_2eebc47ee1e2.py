'Three Stepping Stone Path.\nPlan: Three flattened stones with diminishing sizes progressing upward and right. Shared oval definition, generous separation. Bounds6..42.\nReference: No useful local Lucide stepping-stone match; source oval path and size progression preserved.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a23d3f9-77a9-4a6d-a64f-2eebc47ee1e2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_36/stepping stone_8a23d3f9-77a9-4a6d-a64f-2eebc47ee1e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-oval-stepping-stones'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'oval', 'stepping', 'stones')

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

        for j,(cx,cy,rx,ry) in enumerate(((16,38,10,4),(17,20,7,4),(36,10,6,4))):path(f'stone-{j}',(cx-rx,cy),[((cx+rx,cy),rx,ry,True),((cx-rx,cy),rx,ry,True)],True)
