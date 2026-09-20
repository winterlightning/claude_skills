'Gardening Fork and Trowel.\nPlan: Three-pronged fork and pointed trowel side by side, attached short stems and rounded handles. Bounds6..42.\nReference: Lucide shovel: coherent blade, shaft and loop handle; paired source gardening tools.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d7df087-e715-43c6-9f4d-94aeccae3e19'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/gardening tools_1d7df087-e715-43c6-9f4d-94aeccae3e19.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'garden-fork-and-trowel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('garden', 'fork', 'and', 'trowel')

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

        path('fork',(6,6),[(6,16),((14,24),8,8,False),((22,16),8,8,False),(22,6)])
        self.add_polyline('fork-stem',(14,6),(14,24),(14,30));self.relate('connect','fork','fork-stem')
        box('fork-handle',10,30,18,42,4);self.relate('connect','fork-stem','fork-handle')
        path('blade',(32,16),[(37,6),(42,16),((32,16),5,6,True)],True)
        self.add_line('trowel-stem',(37,22),(37,30));self.relate('connect','blade','trowel-stem')
        box('trowel-handle',33,30,41,42,4);self.relate('connect','trowel-stem','trowel-handle')
