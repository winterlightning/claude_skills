'Building Enveloped by Flame\nPlan: Building foreground with surrounding open flame contour and two window dots.\nReference: Lucide flame: coherent asymmetric tongues; reference building remains the foreground.\nReduction: One window replaces six; flame stays open around building.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b42b12a6-33e7-40fc-99c7-e1ed35cbf68d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/building on fire_b42b12a6-33e7-40fc-99c7-e1ed35cbf68d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'building-enveloped-by-flame'
    keyshape = Keyshape.VRECT_L
    category = "objects"
    keywords = ('building', 'enveloped', 'by', 'flame')

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

        box('building',16,28,32,44,2)
        self.add_bezier('flame',(8,24),((8,20),(10,16),(13,14)),((13,22),(23,19),(23,12)),((23,9),(21,6),(20,4)),((33,9),(34,14),(31,20)),((36,20),(40,18),(40,18)),((40,20),(40,22),(40,24)))
