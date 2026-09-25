'Medieval Castle Fortress.\nSymbol plan: Central triangular-roof tower above a crenellated wall and arched entry. Window omitted. Shared axis24 and repeated wall notches.\nConstruction reference: Lucide castle: structural walls, crenellation and arched entrance.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30413777-603c-404a-a0a6-81ffbe297e90'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/european castle_30413777-603c-404a-a0a6-81ffbe297e90.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'castle-with-roofed-central-tower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('castle', 'with', 'roofed', 'central', 'tower')

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

        self.add_polyline('roof',(14,16),(24,6),(34,16),closed=True)
        self.add_polyline('walls',(6,24),(6,42),(18,42),(18,34))
        self.add_arc('door',(18,34),(30,34),radius_x=6)
        self.add_polyline('right-wall',(30,34),(30,42),(42,42),(42,24))
        self.add_polyline('battlements',(6,24),(14,24),(14,16),(34,16),(34,24),(42,24))
        self.relate('connect','walls','door');self.relate('connect','right-wall','door');self.relate('connect','battlements','roof');self.relate('connect','battlements','walls');self.relate('connect','battlements','right-wall')
