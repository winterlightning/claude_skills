'Camera with Shaking Lines\nPlan: Camera with raised housing and two detached motion strokes.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Two motion strokes remain physical shake marks, not status badges; simplified rectangular body.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5ada276-7815-4d75-9ba7-b74ca81c7919'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/camera settings frame 1_f5ada276-7815-4d75-9ba7-b74ca81c7919.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'camera-with-shaking-lines'
    keyshape = Keyshape.HRECT_L
    category = "primitives-generate"
    keywords = ('camera', 'with', 'shaking', 'lines')

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

        path('camera',(13,18),[(17,18),(20,8),(28,8),(31,18),(35,18),(35,40),(13,40),(13,18)],True)
        circle('lens',24,28,2)
        self.add_bezier('motion-left',(5,10),((5,15),(4,16),(4,21)),((4,26),(5,30),(5,35)))
        self.add_bezier('motion-right',(43,10),((43,15),(44,16),(44,21)),((44,26),(43,30),(43,35)))
