'Round Four Hole Disk with Outer Rim\nPlan: Button disk with four equal small circular holes on shared square spacing.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Omit recessed inner rim to allow four clear circular holes.\nKeyshape: CIRCLE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6fef6aba-fc12-4bb8-91b2-50a289c234d6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/drain_6fef6aba-fc12-4bb8-91b2-50a289c234d6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-four-hole-disk-with-outer-rim'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('round', 'four', 'hole', 'disk', 'with', 'outer', 'rim')

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

        circle('disk',24,24,20)
        for x in (18,30):
            for y in (18,30):circle(f'hole-{x}-{y}',x,y,2)
