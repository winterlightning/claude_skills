'Looped Brass Bugle\nPlan: Bugle with a flared bell and broad lower tube loop; shared mouthpiece run.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Single-line tube loop instead of a narrow double wall; flared bell remains.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c3b1dee-2c1a-4e89-91de-95172d2201db'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/brass_1c3b1dee-2c1a-4e89-91de-95172d2201db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'looped-brass-bugle'
    keyshape = Keyshape.HRECT_L
    category = "objects"
    keywords = ('looped', 'brass', 'bugle')

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

        self.add_polyline('bell',(4,16),(27,16),(44,8),(44,32),(27,24))
        path('tube',(27,24),[(18,24),((18,40),8,8,False),(25,40)])
        self.relate('connect','tube','bell')
