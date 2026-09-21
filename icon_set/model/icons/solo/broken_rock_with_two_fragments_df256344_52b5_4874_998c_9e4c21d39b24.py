'Broken Rock with Two Fragments\nPlan: Angular main rock and two detached triangular fragments; deliberately irregular proportions.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Drop the narrow perspective side face; keep two separate angular fragments.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df256344-52b5-4874-998c-9e4c21d39b24'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/debris_df256344-52b5-4874-998c-9e4c21d39b24.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broken-rock-with-two-fragments'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('broken', 'rock', 'with', 'two', 'fragments')

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

        self.add_polyline('rock',(6,17),(18,6),(27,12),(24,27),(14,34),(6,28),closed=True)
        self.add_polyline('chip-upper',(36,18),(42,26),(34,26))
        self.add_polyline('chip-lower',(31,35),(41,39),(32,42))
