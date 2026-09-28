'Child Reaching Upward\nPlan: Child with circular head aligned above straight torso; exact detached head gap 4; raised right arm.\nReference: Shared human full_body_ref.png: circular head, stroke torso, round-ended limbs.\nReduction: Drop filled anatomy; keep upward reach and spread legs. Head bottom14, torso top22 gives exact4 ink gap.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f603e8f-ebe5-4555-8071-3fba3d73f31b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/child reaching_0f603e8f-ebe5-4555-8071-3fba3d73f31b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'child-reaching-upward'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('child', 'reaching', 'upward')

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

        circle('head',22,9,5)
        self.add_line('torso',(22,22),(22,32))
        self.add_polyline('left-arm',(8,32),(22,22))
        self.add_polyline('right-arm',(22,22),(34,22),(40,8))
        self.add_polyline('legs',(10,42),(22,32),(30,44))
        for p in ('left-arm','right-arm','legs'):self.relate('connect',p,'torso')
        self.relate('connect','left-arm','right-arm')
        self.mark_human_figure('child',head='head',torso='torso',torso_junction='start')
