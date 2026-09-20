'Medical Injection Syringe.\nPlan: Diagonal syringe with T plunger, broad barrel, one graduation and long needle. Bounds6..42.\nConstruction reference: Lucide syringe original and atomic-debug: diagonal barrel, plunger T and continuous needle.\nReduction: Reduce two graduations to one, preserving the source direction.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17b906a6-bcf5-4724-81ac-c48ea8d535e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/syringe 1_17b906a6-bcf5-4724-81ac-c48ea8d535e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'medical-syringe-down-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('medical', 'syringe', 'down', 'right')

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

        def p(x,y):return (48-x,y) if False else (x,y)
        self.add_polyline('barrel',p(20,12),p(12,20),p(26,34),p(34,26),closed=True)
        self.add_line('plunger',p(10,10),p(16,16));self.relate('connect','plunger','barrel')
        self.add_line('grip',p(6,14),p(14,6));self.relate('connect','grip','plunger')
        self.add_line('needle',p(30,30),p(42,42));self.relate('connect','needle','barrel')
        
