'Construction Worker with Hard Hat.\nPlan: Circular jaw below domed hard hat and wide brim; touching broad shoulders. Helmet ribs and arm divisions omitted. Bounds8,4..40,44.\nReference: human_ref/user.svg: circular jaw and broad open shoulders, head ink touching body ink. Lucide hard-hat: domed shell and brim.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3dc4f4ab-97fa-4025-8974-c45802c626d4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/labourer_3dc4f4ab-97fa-4025-8974-c45802c626d4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'construction-worker-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('construction', 'worker', 'bust')

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

        path('helmet',(12,16),[((36,16),12,12,True)])
        self.add_polyline('brim',(8,16),(12,16),(16,16),(32,16),(36,16),(40,16));self.relate('connect','helmet','brim')
        self.add_line('head-left',(16,16),(16,20));self.add_arc('jaw',(16,20),(32,20),radius_x=8,sweep=False);self.add_line('head-right',(32,20),(32,16));self.add_contour('face','head-left','jaw','head-right');self.relate('connect','face','brim')
        self.add_line('body-left',(8,44),(8,40));self.add_arc('body-left-shoulder',(8,40),(20,32),radius_x=12,radius_y=8,sweep=True);self.add_line('body-top',(20,32),(28,32));self.add_arc('body-right-shoulder',(28,32),(40,40),radius_x=12,radius_y=8,sweep=True);self.add_line('body-right',(40,40),(40,44));self.add_contour('body','body-left','body-left-shoulder','body-top','body-right-shoulder','body-right');self.relate('connect','face','body')
