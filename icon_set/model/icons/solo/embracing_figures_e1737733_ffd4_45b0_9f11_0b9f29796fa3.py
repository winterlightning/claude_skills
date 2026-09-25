'Two People Embracing.\nPlan: A large rear figure wraps an arm across a smaller foreground figure.\nConstruction reference: human_ref/user.svg: outlined circular heads and broad shoulders, with exact 8-unit centerline head/body gaps.\nReduction: Small round hand integrated into the arm endpoint; heads separated while retaining the larger rear/smaller front arrangement.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1737733-ffd4-45b0-9f11-0b9f29796fa3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hug_e1737733-ffd4-45b0-9f11-0b9f29796fa3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'embracing-figures'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('embracing', 'figures')

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

        circle('rear-head',19,10,6);circle('front-head',32,24,4)
        path('rear-body',(8,44),[(8,36),((19,24),11,12,True)])
        self.add_line('arm',(8,36),(24,42));self.relate('connect','arm','rear-body')
        path('front-body',(24,44),[(24,42),((32,36),8,6,True),((40,44),8,8,True)])
        self.relate('connect','arm','front-body')
