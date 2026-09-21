'Angry Horned Monster with Raised Arms\nPlan: Rounded monster body with two horns, outward arms, two feet and an angry face; paired parts share axis.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Drop tiny eye ticks; retain angry brows, mouth, horns and limbs.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '154635b8-1d1c-444f-931c-c6c0d2a48acc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/monster_154635b8-1d1c-444f-931c-c6c0d2a48acc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'angry-horned-monster-with-raised-arms'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('angry', 'horned', 'monster', 'with', 'raised', 'arms')

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

        box('body',14,14,34,38,6)
        for k,side in enumerate([-1,1]):
            x=lambda u:24+side*u
            self.add_polyline(f'horn-{k}',(x(8),14),(x(12),6),(x(16),14));self.relate('connect',f'horn-{k}','body')
            self.add_polyline(f'arm-{k}',(x(10),25),(x(18),21),(x(18),29));self.relate('connect',f'arm-{k}','body')
            self.add_polyline(f'foot-{k}',(x(6),38),(x(6),42),(x(10),42));self.relate('connect',f'foot-{k}','body')
        self.add_line('brow-left',(21,23),(22,24));self.add_line('brow-right',(27,23),(26,24))
        self.add_arc('mouth',(20,32),(28,32),radius_x=5,radius_y=3)
