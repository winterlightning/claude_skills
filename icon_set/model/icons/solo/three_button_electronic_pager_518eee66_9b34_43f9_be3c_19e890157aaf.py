'Three-Button Electronic Pager\nPlan: Pager case with blank display band and three equally spaced round controls.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Reduce display frame to one blank display stroke, buttons to dots; drop detached artifact.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '518eee66-9b34-43f9-be3c-19e890157aaf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/pager_518eee66-9b34-43f9-be3c-19e890157aaf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-button-electronic-pager'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('three', 'button', 'electronic', 'pager')

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

        box('case',6,6,42,42,6)
        self.add_line('display',(16,18),(32,18))
        for x in (16,24,32):self.add_dot(f'button-{x}',(x,30))
