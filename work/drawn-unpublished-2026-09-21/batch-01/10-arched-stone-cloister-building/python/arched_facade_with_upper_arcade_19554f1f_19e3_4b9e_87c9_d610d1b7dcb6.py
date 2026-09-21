'Arched Facade with Upper Arcade\nPlan: Wide rounded facade with two upper arch openings and central lower entrance. Width budget is 8+8+8+8+8.\nReference: Lucide landmark: regular architectural rhythm.\nReduction: Two upper arches replace three to maintain spacing.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19554f1f-19e3-4b9e-87c9-d610d1b7dcb6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cloister_19554f1f-19e3-4b9e-87c9-d610d1b7dcb6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arched-facade-with-upper-arcade'
    keyshape = Keyshape.HRECT_L
    category = "objects"
    keywords = ('arched', 'facade', 'with', 'upper', 'arcade')

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

        box('facade',4,8,44,40,4)
        self.add_line('floor',(4,24),(44,24));self.relate('connect','floor','facade')
        for k,x in enumerate([16,32]):
            path(f'window-{k}',(x-4,24),[(x-4,20),((x+4,20),4,4,True),(x+4,24)])
            self.relate('connect',f'window-{k}','floor')
        path('door',(18,40),[(18,37),((30,37),6,5,True),(30,40)])
        self.relate('connect','door','facade')
