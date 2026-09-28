'Human Head Profile.\nSymbol plan: Broad round skull, triangular nose, curved jaw and open neck. Tiny eye omitted. Extremes(8,4)-(40,44).\nConstruction reference: human_ref/user.svg: rounded head vocabulary, adapted to requested profile rather than a front-facing bust.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ecc087a9-51cb-497b-b7d3-3897d52fbe64'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/thrush_ecc087a9-51cb-497b-b7d3-3897d52fbe64.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'rounded-right-facing-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('rounded', 'right', 'facing', 'head', 'profile')

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

        path('head',(14,44),[(14,34),((8,28),6,6,True),(8,20),((24,4),16,16,True),((36,16),12,12,True),(40,26),(34,26),(34,30),((28,36),6,6,True),(24,36),(24,44)])
