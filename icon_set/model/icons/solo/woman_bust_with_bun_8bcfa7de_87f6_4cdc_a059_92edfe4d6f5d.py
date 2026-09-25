'Elderly Woman With Hair Bun.\nPlan: Centered head with parted hair and tall bun, touching broad shoulders. Tiny facial features omitted for clearance. Bounds8,4..40,44.\nReference: human_ref/user.svg: centered circular jaw and broad open shoulders; avatar touching ink rule. Bun preserves source identity.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8bcfa7de-87f6-4cdc-a059-92edfe4d6f5d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_21/granny_8bcfa7de-87f6-4cdc-a059-92edfe4d6f5d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-bust-with-bun'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('woman', 'bust', 'with', 'bun')

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

        path('bun',(20,12),[((28,12),4,8,True)])
        path('hair',(16,20),[(16,16),((20,12),4,4,True),(24,14),(28,12),((32,16),4,4,True),(32,20)])
        self.add_arc('jaw',(32,20),(16,20),radius_x=8,sweep=True)
        self.relate('connect','hair','jaw');self.relate('connect','bun','hair')
        self.add_line('body-left',(8,44),(8,40));self.add_arc('body-left-shoulder',(8,40),(20,32),radius_x=12,radius_y=8,sweep=True)
        self.add_line('body-top',(20,32),(28,32));self.add_arc('body-right-shoulder',(28,32),(40,40),radius_x=12,radius_y=8,sweep=True);self.add_line('body-right',(40,40),(40,44))
        self.add_contour('body','body-left','body-left-shoulder','body-top','body-right-shoulder','body-right');self.relate('connect','jaw','body')
