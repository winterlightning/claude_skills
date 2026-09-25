'Cloven Hoof Print\nPlan: Mirrored long cloven impressions; broad lower ends and narrow rounded tips preserve hoof print.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2f4e802-1157-4a3d-8764-11a7b6e6d6fd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/animal print two fingers_f2f4e802-1157-4a3d-8764-11a7b6e6d6fd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloven-hoof-print'
    keyshape = Keyshape.VRECT_L
    category = "primitives-generate"
    keywords = ('cloven', 'hoof', 'print')

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

        for side in [-1,1]:
            x=lambda a:24+side*a
            name='left' if side<0 else 'right'
            self.add_bezier(name,(x(7),4),((x(4),4),(x(4),12),(x(4),22)),((x(4),34),(x(4),44),(x(10),44)),((x(16),44),(x(16),34),(x(16),28)),((x(16),18),(x(11),4),(x(7),4)))
            self.add_contour(name+'-outline',name,closed=True)
