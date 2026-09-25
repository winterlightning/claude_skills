'Three Person User Group.\nPlan: Three circular heads with curved shoulders; smaller side figures join behind the central shoulders.\nConstruction reference: Shared user.svg: circular heads with smooth shoulder arcs.\nReduction: Three heads retained; side shoulders join the central silhouette at true nodes. All head-to-own-shoulder centerline gaps are exactly 8.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '492c5a6b-bbb1-4d5d-8fb7-a4836fc2ec91'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/people_492c5a6b-bbb1-4d5d-8fb7-a4836fc2ec91.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-person-user-group'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('three', 'person', 'user', 'group')

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

        circle('head',24,12,4)
        path('shoulders',(14,40),[(14,34),((24,24),10,10,True),((34,34),10,10,True),(34,40)])
        for side,x in [('left',8),('right',40)]:circle(f'{side}-head',x,18,4)
        path('left-body',(4,40),[(4,34),((12,34),4,4,True),(14,34)])
        path('right-body',(44,40),[(44,34),((36,34),4,4,False),(34,34)])
        self.relate('connect','left-body','shoulders');self.relate('connect','right-body','shoulders')
