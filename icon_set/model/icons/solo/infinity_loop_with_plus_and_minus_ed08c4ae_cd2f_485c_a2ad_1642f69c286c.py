'Infinity Loop with Plus and Minus\nPlan: Infinity logo with crossing lobes, minus in left and plus in right; preserve all logo marks.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: HRECT_M; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed08c4ae-cd2f-485c-a2ad-1642f69c286c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/arduino plus minus_ed08c4ae-cd2f-485c-a2ad-1642f69c286c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'infinity-loop-with-plus-and-minus'
    keyshape = Keyshape.HRECT_M
    category = "objects"
    keywords = ('infinity', 'loop', 'with', 'plus', 'and', 'minus')

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

        self.add_bezier('loop',(24,24),((18,14),(16,10),(11,10)),((2,10),(2,38),(11,38)),((16,38),(18,34),(24,24)),((30,14),(32,10),(37,10)),((46,10),(46,38),(37,38)),((32,38),(30,34),(24,24)))
        self.add_contour('infinity','loop',closed=True)
        self.add_line('minus',(10,24),(14,24))
        self.add_line('plus-h',(34,24),(38,24));self.add_line('plus-v',(36,22),(36,26));self.relate('connect','plus-h','plus-v')
