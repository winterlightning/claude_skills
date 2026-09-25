'Car Front with Proximity Waves\nPlan: Front half of a car faces left with two proximity arcs ahead.\nReference: Lucide car: open body around wheel.\nReduction: Two sensing arcs retained; clipped rear stays cropped as in reference.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '474e097e-5638-4708-948a-6b1e5e6bcd8e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/auto pilot car rear warning_474e097e-5638-4708-948a-6b1e5e6bcd8e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-front-with-proximity-waves'
    keyshape = Keyshape.HRECT_L
    category = "primitives-generate"
    keywords = ('car', 'front', 'with', 'proximity', 'waves')

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

        self.add_polyline('body',(20,21),(29,21),(37,8),(44,8),(44,21),(29,21))
        circle('wheel',31,35,5)
        self.add_line('sill',(36,35),(44,35));self.relate('connect','sill','wheel')
        self.add_arc('wave-outer',(10,8),(10,36),radius_x=6,radius_y=14,sweep=False)
