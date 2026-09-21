'Trapezoidal Lamp with Three Light Streaks\nPlan: Slanted lamp body with three progressively longer detached light streaks.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: All three light streaks retained, placed beyond slanted lamp edge.\nKeyshape: HRECT_M; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0db36fbc-6adc-40a4-a40b-474822ffc30a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beam_0db36fbc-6adc-40a4-a40b-474822ffc30a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'trapezoidal-lamp-with-three-light-streaks'
    keyshape = Keyshape.HRECT_M
    category = "objects"
    keywords = ('trapezoidal', 'lamp', 'with', 'three', 'light', 'streaks')

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

        self.add_polyline('lamp',(4,10),(29,10),(21,38),(4,38),closed=True)
        for i,(x,y) in enumerate([(39,14),(36,24),(33,34)]):self.add_line(f'beam-{i}',(x,y),(44,y))
