'Liquid Soap Pump Bottle.\nPlan: Rounded soap bottle, slim pump stem and left bent dispenser. Bounds10,4..38,44.\nConstruction reference: Lucide soap-dispenser-droplet original/atomic-debug: rounded body and attached pump.\nReduction: Reduce separate collar to a single pump stem.\nKeyshape: VRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac1f1712-7697-4b0c-9e64-f9e8bf3c5598'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bottle soap_ac1f1712-7697-4b0c-9e64-f9e8bf3c5598.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'soap-pump-bottle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('soap', 'pump', 'bottle')

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

        box('bottle',10,16,38,44,6)
        self.add_line('stem',(24,16),(24,4));self.relate('connect','stem','bottle')
        self.add_polyline('pump',(12,8),(16,4),(34,4));self.relate('connect','stem','pump')
