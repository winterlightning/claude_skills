'Three Arch Bridge over Waves\nPlan: Three arch spans under a deck, above one coherent wave row.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: One water wave row replaces the two original rows.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9988cbd0-ac55-4989-953b-f0032677f229'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/causeway_9988cbd0-ac55-4989-953b-f0032677f229.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-arch-bridge-over-waves'
    keyshape = Keyshape.HRECT_L
    category = "objects"
    keywords = ('three', 'arch', 'bridge', 'over', 'waves')

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

        self.add_line('deck',(4,8),(44,8))
        for k,x in enumerate([4,20,36]):
            path(f'arch-{k}',(x,27),[(x,22),((x+8,22),4,5,True),(x+8,27)])
        self.add_bezier('water',(4,40),((7,40),(7,36),(11,36)),((15,36),(15,40),(19,40)),((23,40),(23,36),(27,36)),((31,36),(31,40),(35,40)),((39,40),(40,36),(44,36)))
