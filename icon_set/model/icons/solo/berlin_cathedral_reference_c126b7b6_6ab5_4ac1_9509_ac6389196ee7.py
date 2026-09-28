'Berlin Cathedral Landmark Building.\nPlan: Two tall pointed towers flank a shorter gabled nave; left cross remains. Tower walls preserve the architecture.\nConstruction reference: Lucide church: structural gable and towers.\nReduction: Door, window and tower seams removed to keep three clear architectural bays; source landmark attribution remains uncertain.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c126b7b6-6ab5-4ac1-9509-ac6389196ee7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/landmark berlin cathedral_c126b7b6-6ab5-4ac1-9509-ac6389196ee7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'berlin-cathedral-reference'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('berlin', 'cathedral', 'reference')

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

        self.add_polyline('building',(6,42),(6,18),(12,12),(18,18),(18,26),(24,18),(30,26),(30,18),(36,12),(42,18),(42,42),(30,42),(18,42),closed=True)
        for x in (18,30):self.add_line(f'tower-wall-{x}',(x,26),(x,42));self.relate('connect',f'tower-wall-{x}','building')
        self.add_line('cross-stem',(12,6),(12,12));self.relate('connect','cross-stem','building')
        self.add_line('crossbar',(8,8),(16,8));self.relate('connect','crossbar','cross-stem')
