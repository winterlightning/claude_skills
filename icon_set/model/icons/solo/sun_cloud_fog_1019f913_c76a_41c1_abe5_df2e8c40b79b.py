'Sun Behind Cloud with Wind.\nPlan: Small sun partially overlapped by broad cloud, two low fog lines. Rays omitted to open spacing. Bounds6..42.\nReference: Lucide cloud-sun and wind: integrated weather silhouette with two separate horizontal fog strokes.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1019f913-c76a-41c1-abe5-df2e8c40b79b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/weather cloud sun wind 2_1019f913-c76a-41c1-abe5-df2e8c40b79b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-cloud-fog'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sun', 'cloud', 'fog')

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

        path('outline',(12,18),[((6,12),6,6,True),((12,6),6,6,True),((18,12),6,6,True),((30,12),6,4,True),((42,18),12,6,True),((36,24),6,6,True),(18,24),((12,18),6,6,True)],True)
        path('sun-seam',(18,12),[((12,18),6,6,True)]);self.relate('connect','sun-seam','outline')
        self.add_line('fog-upper',(8,33),(38,33));self.add_line('fog-lower',(14,42),(32,42))
