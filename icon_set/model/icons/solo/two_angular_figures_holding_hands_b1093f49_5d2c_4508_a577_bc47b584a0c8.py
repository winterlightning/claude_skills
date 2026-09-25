'Two People Holding Hands.\nPlan: Two stick figures join their inner hands.\nConstruction reference: human_ref/full_body_ref.png: simple limbs, circular heads and torso-aligned exact detached head gap.\nReduction: Angular outline torsos translated to the shared stick-figure vocabulary.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1093f49-5d2c-4508-a577-bc47b584a0c8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/group 1_b1093f49-5d2c-4508-a577-bc47b584a0c8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-angular-figures-holding-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('two', 'angular', 'figures', 'holding', 'hands')

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

        for x in (14,34):
         circle(f'head-{x}',x,10,4)
         self.add_line(f'torso-{x}',(x,22),(x,32))
         self.add_polyline(f'legs-{x}',(x-6,42),(x,32),(x+6,42))
         self.relate('connect',f'torso-{x}',f'legs-{x}')
         self.mark_human_figure(f'person-{x}',head=f'head-{x}',torso=f'torso-{x}',torso_junction='start')
        self.add_polyline('arms',(6,22),(14,22),(24,28),(34,22),(42,22))
        for x in (14,34):self.relate('connect','arms',f'torso-{x}')
