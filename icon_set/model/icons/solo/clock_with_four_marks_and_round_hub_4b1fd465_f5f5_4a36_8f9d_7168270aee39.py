'Clock with Four Marks and Round Hub\nPlan: Circular face, rightward hands and circular hub; cardinal hour marks omitted to open the face.\nReference: Lucide clock: one circular face and minimal central hands.\nReduction: Omit four small tick marks to keep legal interior spacing.\nKeyshape: CIRCLE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b1fd465-f5f5-4a36-8f9d-7168270aee39'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dial_4b1fd465-f5f5-4a36-8f9d-7168270aee39.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clock-with-four-marks-and-round-hub'
    keyshape = Keyshape.CIRCLE
    category = "primitives-generate"
    keywords = ('clock', 'with', 'four', 'marks', 'and', 'round', 'hub')

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

        circle('face',24,24,20)
        self.add_polyline('hands',(32,16),(24,24),(32,32))
