'Customer Support Agent.\nPlan: Blank circular jaw, broad headphone band and short side ear strokes above touching open shoulders. Inner headband line omitted. Bounds8,4..40,44.\nReference: human_ref/user.svg: circular jaw and broad shoulders, zero head/body ink gap. Lucide headphones: outer headband and side ear connections.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a84678ef-8798-47d5-88aa-ee92e6ab8026'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_22/headphones man_a84678ef-8798-47d5-88aa-ee92e6ab8026.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'headphones-user-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('headphones', 'user', 'bust')

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

        path('band',(8,28),[(8,20),((40,20),16,16,True),(40,28)])
        self.add_line('ear-left',(8,20),(16,20));self.add_line('ear-right',(32,20),(40,20));self.relate('connect','ear-left','band');self.relate('connect','ear-right','band')
        self.add_arc('jaw',(16,20),(32,20),radius_x=8,sweep=False);self.relate('connect','jaw','ear-left');self.relate('connect','jaw','ear-right')
        self.add_line('body-left',(8,44),(8,40));self.add_arc('body-left-shoulder',(8,40),(20,32),radius_x=12,radius_y=8,sweep=True);self.add_line('body-top',(20,32),(28,32));self.add_arc('body-right-shoulder',(28,32),(40,40),radius_x=12,radius_y=8,sweep=True);self.add_line('body-right',(40,40),(40,44));self.add_contour('body','body-left','body-left-shoulder','body-top','body-right-shoulder','body-right');self.relate('connect','jaw','body')
