'Low Vacuum with Tall Curved Hose\nPlan: Low canister and round wheel below tall looping hose, with right floor nozzle.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Single-line hose and floor nozzle; preserve low rounded canister and wheel.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73b9d387-6248-460f-a92b-023ea2dc33b8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cleaning vacuum 2_73b9d387-6248-460f-a92b-023ea2dc33b8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-vacuum-with-tall-curved-hose'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('low', 'vacuum', 'with', 'tall', 'curved', 'hose')

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

        path('body',(8,39),[(6,26),(14,26),((26,36),12,10,True),(14,39)])
        circle('wheel',11,39,3);self.relate('connect','wheel','body')
        self.add_bezier('hose',(23,29),((26,23),(24,17),(24,12)),((24,4),(36,4),(36,12)),((36,22),(36,30),(36,34)));self.relate('connect','hose','body')
        self.add_polyline('nozzle',(36,34),(42,34),(42,42),(34,42))
        self.relate('connect','hose','nozzle')
