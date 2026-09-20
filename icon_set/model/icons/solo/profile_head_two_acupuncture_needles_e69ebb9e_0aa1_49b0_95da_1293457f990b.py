'Head with Acupuncture Needles.\nPlan: Right-facing profile with two separate round-headed acupuncture needles inserted into the scalp.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Eye and ear omitted; both round-headed needles remain separated and meet actual scalp nodes.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e69ebb9e-0aa1-49b0-95da-1293457f990b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/acupuncture head_e69ebb9e-0aa1-49b0-95da-1293457f990b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'profile-head-two-acupuncture-needles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('profile', 'head', 'two', 'acupuncture', 'needles')

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

        path('head',(20,42),[(20,38),(14,32),(14,30),((24,20),10,10,True),((34,30),10,10,True),(42,34),(34,36),(34,42)])
        circle('pin-one',8,8,2);circle('pin-two',24,8,2)
        self.add_line('needle-one',(10,8),(14,30));self.relate('connect','needle-one','pin-one');self.relate('connect','needle-one','head')
        self.add_line('needle-two',(24,10),(24,20));self.relate('connect','needle-two','pin-two');self.relate('connect','needle-two','head')
