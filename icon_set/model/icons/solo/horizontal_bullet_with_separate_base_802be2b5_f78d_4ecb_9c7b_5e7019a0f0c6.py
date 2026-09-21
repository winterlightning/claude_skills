'Horizontal Bullet with Separate Base\nPlan: Horizontal projectile; rear bracket separated by eight units from body. Curved nose is a coherent oval half.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: HRECT_M; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '802be2b5-f78d-4ecb-9c7b-5e7019a0f0c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bullet_802be2b5-f78d-4ecb-9c7b-5e7019a0f0c6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-bullet-with-separate-base'
    keyshape = Keyshape.HRECT_M
    category = "objects"
    keywords = ('horizontal', 'bullet', 'with', 'separate', 'base')

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

        self.add_polyline('base',(8,10),(4,10),(4,38),(8,38))
        path('bullet',(17,10),[(28,10),((44,24),16,14,True),((28,38),16,14,True),(17,38),(17,10)],True)
