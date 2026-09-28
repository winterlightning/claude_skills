'User Profile Icon.\nPlan: Centered circular head radius8 at24,12; shoulder top24, exactly4 centerline gap and0 ink gap. Broad curved shoulders and open bottom. Bounds8,4..40,44.\nReference: human_ref/user.svg: circular head, broad curved shoulders, short sides; icon-avatar touching-ink rule supersedes reference gap.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6640b907-0d18-4814-a18c-44d7866af830'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/dude_6640b907-0d18-4814-a18c-44d7866af830.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-bust-round-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('person', 'bust', 'round', 'head')

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

        self.add_arc('head-top',(16,12),(32,12),radius_x=8,sweep=True)
        self.add_arc('jaw',(32,12),(16,12),radius_x=8,sweep=True)
        self.add_contour('head','head-top','jaw',closed=True)
        self.add_line('body-left',(8,44),(8,36))
        self.add_arc('body-left-shoulder',(8,36),(20,24),radius_x=12,sweep=True)
        self.add_line('body-top',(20,24),(28,24))
        self.add_arc('body-right-shoulder',(28,24),(40,36),radius_x=12,sweep=True)
        self.add_line('body-right',(40,36),(40,44))
        self.add_contour('body','body-left','body-left-shoulder','body-top','body-right-shoulder','body-right')
        self.relate('connect','head','body')
