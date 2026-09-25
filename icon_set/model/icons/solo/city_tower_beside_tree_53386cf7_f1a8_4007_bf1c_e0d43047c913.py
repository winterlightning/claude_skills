'City Tower beside Tree\nPlan: Tall urban building at left with two windows; round tree right and shared ground.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Drop low foreground block and tree branches, keep tower/tree scene.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53386cf7-f1a8-4007-bf1c-e0d43047c913'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/outdoors 1_53386cf7-f1a8-4007-bf1c-e0d43047c913.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'city-tower-beside-tree'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "outdoors"
    categories = ("outdoors", "primitive", "primitives")
    keywords = ('city', 'tower', 'beside', 'tree')

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

        self.add_polyline('building',(6,42),(6,14),(22,14),(22,42))
        self.add_line('antenna',(14,6),(14,14));self.relate('connect','antenna','building')
        for y in (24,34):self.add_line(f'window-{y}',(14,y),(14,y))
        circle('tree',36,26,6)
        self.add_line('trunk',(36,32),(36,42));self.relate('connect','trunk','tree')
        self.add_line('ground',(6,42),(42,42));self.relate('connect','ground','building');self.relate('connect','ground','trunk')
