'Child Seated in Safety Chair\nPlan: Seated child with circular head and bent torso inside open L-shaped safety seat.\nReference: Shared human full_body_ref.png seated figure: minimal limb construction.\nReduction: Drop thick chair enclosure; retain protective back and bent seated pose, exact4 head gap.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e56f665-c251-4caa-8739-13258be70d06'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/child seat anchor 1_3e56f665-c251-4caa-8739-13258be70d06.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'child-seated-in-safety-chair'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('child', 'seated', 'in', 'safety', 'chair')

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
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        circle('head',24,12,4)
        self.add_line('torso',(24,24),(24,32))
        self.add_polyline('legs',(24,32),(36,32),(40,40))
        self.add_line('arm',(24,24),(36,24));self.relate('connect','arm','torso');self.relate('connect','legs','torso')
        path('seat',(4,8),[(8,34),((14,40),6,6,False),(44,40)])
        self.relate('connect','seat','legs')
        self.mark_human_figure('child',head='head',torso='torso',torso_junction='start')
