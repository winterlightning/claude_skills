'Wharf over Water.\n\nSymbol plan: Two repeated8-unit posts support deck edges y18/y26. Water scallops run between y35 and y38, with9 units above their crest to the lower deck.\nConstruction reference: No useful Lucide subject match; repeated structural rectangles and smooth water arc.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d1840e4-96fe-4794-ab4a-27ad261cb543'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/wharf_7d1840e4-96fe-4794-ab4a-27ad261cb543.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'wharf-above-water'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('wharf', 'above', 'water')

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

        for j,x in enumerate((4,36)):
            self.add_polyline(f'post-{j}',(x,10),(x+8,10),(x+8,18),(x+8,26),(x+8,38),(x,38),(x,26),(x,18),closed=True)
        for name,y in [('deck-top',18),('deck-bottom',26)]:
            self.add_line(name,(12,y),(36,y))
            self.relate('connect',name,'post-0')
            self.relate('connect',name,'post-1')
        path('water',(12,38),[((24,38),6,3,True),((36,38),6,3,True)])
        self.relate('connect','water','post-0')
        self.relate('connect','water','post-1')
