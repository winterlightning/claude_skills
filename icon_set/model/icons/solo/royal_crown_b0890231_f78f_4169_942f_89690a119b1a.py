'Simple Royal Crown.\nPlan: Three-point crown with tallest central peak and broad flat base. Mirrored x24, exact4,8..44,40. No jewels or extra band.\nReference: Lucide crown: pointed peaks and valleys in one contour; source plain royal silhouette retained.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0890231-f78f-4169-942f-89690a119b1a'
SOURCE_PATH = 'pictographic-primitives/other/crown_b0890231-f78f-4169-942f-89690a119b1a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'royal-crown'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('royal', 'crown')

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

        self.add_polyline('crown',(4,14),(14,24),(24,8),(34,24),(44,14),(40,40),(8,40),closed=True)
