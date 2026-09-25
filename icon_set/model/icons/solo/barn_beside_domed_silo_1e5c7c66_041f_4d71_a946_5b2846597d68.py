'Barn and Silo.\nPlan: Barn and adjoining silo form one farm scene; shared baseline and silo seam.\nConstruction reference: Lucide church: coherent building outline and arched entry.\nReduction: Tiny loft window omitted.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e5c7c66-041f-4d71-a946-5b2846597d68'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/farm_1e5c7c66-041f-4d71-a946-5b2846597d68.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'barn-beside-domed-silo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('barn', 'beside', 'domed', 'silo')

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

        self.add_polyline('barn',(4,40),(4,22),(16,12),(28,22),(28,40),(20,40),(12,40),closed=True)
        path('silo',(28,40),[(28,16),((44,16),8,8,True),(44,40),(28,40)],True)
        self.relate('connect','barn','silo')
        self.add_line('silo-seam',(28,16),(44,16));self.relate('connect','silo-seam','silo')
        path('door',(12,40),[(12,32),((20,32),4,4,True),(20,40)])
        self.relate('connect','door','barn')
