'Samosas on a Plate.\nPlan: Two overlapping triangular samosas sit on a shallow curved plate. The rear base joins the front edge; small filling marks are omitted.\nReference: No useful Lucide samosa match; coherent triangular food silhouettes and wide oval plate from source.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb2a2e58-efc6-41ca-9022-2f437cd1717f'
SOURCE_PATH = 'pictographic-primitives/other/samosa_fb2a2e58-efc6-41ca-9022-2f437cd1717f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'samosas-on-a-plate'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('samosas', 'on', 'a', 'plate')

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

        self.add_polyline('front',(6,30),(16,10),(22,22),(24,26),(26,30),closed=True)
        self.add_polyline('rear',(22,22),(30,8),(40,22),(22,22));self.relate('connect','front','rear')
        path('plate',(6,30),[(4,38),((24,40),20,2,False),((44,38),20,2,False),(40,22)]);self.relate('connect','plate','front');self.relate('connect','plate','rear')
