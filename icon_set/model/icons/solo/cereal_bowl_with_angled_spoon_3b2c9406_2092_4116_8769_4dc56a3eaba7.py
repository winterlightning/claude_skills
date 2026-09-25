'Cereal Bowl with Angled Spoon\nPlan: Semicircular bowl with horizontal rim; angled spoon attaches at rim.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Remove double oval rim and contents; retain bowl depth and angled spoon.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b2c9406-2092-4116-8769-4dc56a3eaba7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/breakfast cereal bowl spoon_3b2c9406-2092-4116-8769-4dc56a3eaba7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cereal-bowl-with-angled-spoon'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('cereal', 'bowl', 'with', 'angled', 'spoon')

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

        path('bowl',(4,24),[(44,24),((4,24),20,16,True)],True)
        self.add_line('spoon',(30,24),(38,8));self.relate('connect','bowl','spoon')
