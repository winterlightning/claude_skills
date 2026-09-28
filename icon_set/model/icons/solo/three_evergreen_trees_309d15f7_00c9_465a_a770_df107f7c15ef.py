'Three Evergreen Trees.\nPlan: Three triangular evergreen canopies, central tree forward with a visible trunk.\nConstruction reference: Lucide trees inspected for grove grouping; source triangular conifers retained.\nReduction: Side trunks and tier divisions omitted; three pointed canopies and central trunk retained.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '309d15f7-00c9-465a-a770-df107f7c15ef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/forest_309d15f7-00c9-465a-a770-df107f7c15ef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-evergreen-trees'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'evergreen', 'trees')

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

        path('front',(24,8),[(30,20),(32,24),(36,32),(24,32),(12,32),(16,24),(18,20),(24,8)],True)
        path('left',(16,24),[(4,24),(10,12),(18,20)]);path('right',(32,24),[(44,24),(38,12),(30,20)])
        self.relate('connect','front','left');self.relate('connect','front','right')
        self.add_line('trunk',(24,32),(24,40));self.relate('connect','trunk','front')
