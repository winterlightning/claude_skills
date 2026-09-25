'Tent beside Round Crown Tree\nPlan: Round crowned tree at right and triangular tent at left, shared ground.\nReference: Lucide tent-tree: natural campsite scene, re-authored with round crown.\nReduction: Remove branching twig detail and nested entrance triangle.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ec0d821-df70-49aa-962a-1a4942629194'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/camping tent forest_5ec0d821-df70-49aa-962a-1a4942629194.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tent-beside-round-crown-tree'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('tent', 'beside', 'round', 'crown', 'tree')

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

        circle('crown',32,16,10)
        self.add_line('trunk',(32,16),(32,42));self.relate('connect','trunk','crown')
        self.add_polyline('tent',(6,42),(16,24),(24,42))
        
        self.add_line('ground',(6,42),(42,42));self.relate('connect','ground','trunk');self.relate('connect','ground','tent')
