'Two Terminal Car Battery\nPlan: Rectangular battery with raised terminals and intrinsic polarity operators.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Polarity operators are intrinsic battery markings, not letters or numerals; retained.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5bbb1d0-0733-4fe9-aa3d-53b1775cb2d5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car tool battery_f5bbb1d0-0733-4fe9-aa3d-53b1775cb2d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-terminal-car-battery'
    keyshape = Keyshape.HRECT_L
    category = "primitives-generate"
    keywords = ('two', 'terminal', 'car', 'battery')

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

        box('body',4,16,44,40,3)
        for i,x in enumerate([8,32]):
         self.add_polyline(f'terminal-{i}',(x,16),(x,8),(x+8,8),(x+8,16));self.relate('connect',f'terminal-{i}','body')
        self.add_line('minus',(13,28),(17,28))
        self.add_line('plus-h',(29,28),(35,28));self.add_line('plus-v',(32,25),(32,31));self.relate('connect','plus-h','plus-v')
