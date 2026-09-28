'Domed Canister Vacuum with Hose\nPlan: Domed canister with large lower wheel and high arching hose.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Omit neck fitting and double-wall hose; keep dome, wheel and nozzle.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b34fe2ce-a231-4d6b-854b-56f36cacf58b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cleaning vacuum 1_b34fe2ce-a231-4d6b-854b-56f36cacf58b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'domed-canister-vacuum-with-hose'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('domed', 'canister', 'vacuum', 'with', 'hose')

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

        path('body',(6,37),[(6,26),((24,26),9,9,True),(24,32)])
        circle('wheel',19,37,5);self.relate('connect','wheel','body')
        self.add_line('base',(6,37),(14,37));self.relate('connect','base','body');self.relate('connect','base','wheel')
        self.add_bezier('hose',(15,17),((15,6),(20,6),(25,6)),((36,6),(36,11),(36,17)),((36,24),(36,28),(36,34)));self.relate('connect','hose','body')
        self.add_polyline('head',(33,42),(33,34),(41,34),(42,42),(33,42));self.relate('connect','head','hose')
