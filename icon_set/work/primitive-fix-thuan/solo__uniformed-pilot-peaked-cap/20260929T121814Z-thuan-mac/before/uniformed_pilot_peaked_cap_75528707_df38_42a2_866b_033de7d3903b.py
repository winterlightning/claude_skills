'Uniformed Airline Pilot.\nPlan: Pilot cap above circular lower face and broad curved shoulders. Circular jaw center24,20 r8; body-top32, exact zero ink gap.\nConstruction reference: human_ref/user.svg circular jaw and broad curved shoulders; source peaked cap retained.\nReduction: Omit cap band, lapels and sleeve divisions to preserve clear face and uniform seam.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75528707-df38-42a2-866b-033de7d3903b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/airman_75528707-df38-42a2-866b-033de7d3903b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'uniformed-pilot-peaked-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('uniformed', 'pilot', 'peaked', 'cap')

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

        self.add_polyline('cap',(8,12),(24,4),(40,12),(32,20),(16,20),closed=True)
        self.add_arc('face',(32,20),(16,20),radius_x=8)
        self.relate('connect','cap','face')
        self.add_arc('body-left-shoulder',(8,44),(20,32),radius_x=12)
        self.add_line('body-top',(20,32),(28,32))
        self.add_arc('body-right-shoulder',(28,32),(40,44),radius_x=12)
        self.add_contour('body','body-left-shoulder','body-top','body-right-shoulder')
        self.relate('connect','face','body')
        self.add_line('body-seam',(24,32),(24,44));self.relate('connect','body','body-seam')
