'Two People Hugging.\nPlan: Two round-headed busts with a diagonal arm reaching across the neighboring person.\nConstruction reference: human_ref/user.svg: round heads and broad shoulders; source diagonal embrace retained.\nReduction: Lower inner body outlines omitted around the crossing arm.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9273110-9f8b-46ca-8cfa-ca10641cf14b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hugger_e9273110-9f8b-46ca-8cfa-ca10641cf14b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'side-by-side-hug'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('side', 'by', 'side', 'hug')

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

        for x in (14,34):circle(f'head-{x}',x,14,6)
        path('left-body',(4,40),[(4,38),((14,28),10,10,True)])
        path('right-body',(34,28),[((44,38),10,10,True),(44,40)])
        self.add_line('embracing-arm',(14,28),(34,40));self.relate('connect','embracing-arm','left-body')
