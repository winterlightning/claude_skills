'Toothed Circular Saw Blade\nPlan: Eight asymmetric blade teeth derived by quarter-turn repetition; centered arbor hole.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Eight large teeth replace the dense original tooth ring.\nKeyshape: CIRCLE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31ce41a9-a1f2-4b30-8759-5f35eccfe310'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/circular saw_31ce41a9-a1f2-4b30-8759-5f35eccfe310.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toothed-circular-saw-blade'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('toothed', 'circular', 'saw', 'blade')

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

        base=[(24,4),(24,10),(34,7),(32,14)]
        points=[]
        for turn in range(4):
            for x,y in base:
                x-=24;y-=24
                for _ in range(turn):x,y=-y,x
                points.append((24+x,24+y))
        self.add_polyline('teeth',*points,closed=True)
        circle('arbor',24,24,4)
