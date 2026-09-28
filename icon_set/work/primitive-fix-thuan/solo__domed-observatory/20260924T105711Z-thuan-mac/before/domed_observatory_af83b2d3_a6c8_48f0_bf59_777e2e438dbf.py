'Domed Observatory\nPlan: Domed observatory on rectangular base with projecting telescope tube.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Omit doubled base band and tube collar; preserve projecting telescope and dome.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af83b2d3-a6c8-48f0-bf59-777e2e438dbf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/observatory_af83b2d3-a6c8-48f0-bf59-777e2e438dbf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'domed-observatory'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('domed', 'observatory')

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

        path('dome',(6,30),[((38,30),16,20,True)])
        self.add_polyline('base',(6,30),(42,30),(42,42),(6,42),(6,30));self.relate('connect','base','dome')
        self.add_polyline('tube',(29,14),(36,6),(42,13),(35,20));self.relate('connect','tube','dome')
