'Person Wearing VR Headset.\nPlan: Circular head interrupted by broad rectangular VR visor, above curved touching shoulders. Jaw24,22 r8 bottom30, bodytop34.\nConstruction reference: human_ref/user.svg circular jaw and rounded shoulders; source eye-covering VR visor.\nReduction: Omit visor nose notch and neck crease.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1bc0a357-ae8c-5287-a849-d7b91c2e7aff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/device wearable vr goggles_1bc0a357-ae8c-5287-a849-d7b91c2e7aff.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-wearing-vr-headset'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('person', 'wearing', 'vr', 'headset')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
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

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        self.add_arc('crown',(16,12),(32,12),radius_x=8)
        path('visor',(11,12),[(16,12),(32,12),(37,12),((40,15),3,3,True),(40,19),((37,22),3,3,True),(32,22),(16,22),(11,22),((8,19),3,3,True),(8,15),((11,12),3,3,True)],True)
        self.add_arc('jaw',(32,22),(16,22),radius_x=8)
        self.relate('connect','visor','crown');self.relate('connect','visor','jaw')
        self.add_arc('body-left',(8,44),(18,34),radius_x=10)
        self.add_line('body-top',(18,34),(30,34))
        self.add_arc('body-right',(30,34),(40,44),radius_x=10)
        self.add_contour('body','body-left','body-top','body-right');self.relate('connect','jaw','body')
