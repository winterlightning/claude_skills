'Hooded Person with Blank Face\nPlan: Hooded circular face centered above touching curved shoulders; open hood sides merge at shoulders.\nReference: Human user.svg and avatar rule: circular face, curved shoulders, head ink touching body ink.\nReduction: Drop sleeve lines; retain hood and jacket center seam.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4eebbb0e-3d47-4014-a9b8-95819896ada8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/rogue_4eebbb0e-3d47-4014-a9b8-95819896ada8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hooded-person-with-blank-face'
    keyshape = Keyshape.VRECT_L
    human_construction = "bust"
    category = "objects"
    keywords = ('hooded', 'person', 'with', 'blank', 'face')

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

        circle('face',24,20,6)
        self.add_bezier('hood',(12,33),((8,29),(8,25),(8,22)),((8,15),(18,4),(24,4)),((30,4),(40,15),(40,22)),((40,25),(40,29),(36,33)))
        self.add_bezier('shoulders',(8,44),((8,38),(9,35),(12,33)),((15,31),(20,30),(24,30)),((28,30),(33,31),(36,33)),((39,35),(40,38),(40,44)))
        self.relate('connect','face','shoulders');self.relate('connect','hood','shoulders')
        self.add_line('seam',(24,39),(24,44))
