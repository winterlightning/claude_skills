'Person Wearing a Wide Brim Hat.\nPlan: Centered circular jaw radius8, hat with wide brim, broad curved shoulder arc. Hat top4, body bottom44, x8..40. Jaw bottom30, shoulder top34: tangent ink contact0. Omit neckline seam.\nReference: human_ref/user.svg for rounded shoulders/circular face; icon-avatar contact rule; Lucide hat-glasses for connected crown/brim.\nKeyshape: VRECT_L; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7572d6aa-7ab3-420a-be2f-138583adcc4b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/explorer_7572d6aa-7ab3-420a-be2f-138583adcc4b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-wearing-wide-brim-hat-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('person', 'wearing', 'wide', 'brim', 'hat', 'solo')
    human_construction = "bust"

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

        path('crown',(14,14),[(16,4),(32,4),(34,14)])
        self.add_polyline('brim',(8,14),(14,14),(16,14),(32,14),(34,14),(40,14));self.relate('connect','crown','brim')
        self.add_line('head-left',(16,14),(16,22))
        self.add_arc('jaw',(16,22),(32,22),radius_x=8,radius_y=8,sweep=False)
        self.add_line('head-right',(32,22),(32,14))
        self.add_contour('head','head-left','jaw','head-right')
        self.relate('connect','head','brim')
        self.add_arc('body-top',(8,44),(40,44),radius_x=16,radius_y=10,sweep=True)
        self.relate('connect','head','body-top')
