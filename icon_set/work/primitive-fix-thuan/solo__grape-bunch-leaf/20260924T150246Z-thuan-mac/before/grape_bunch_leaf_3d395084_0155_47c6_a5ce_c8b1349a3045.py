'Grape Bunch with Leaf\nPlan: Six grapes in 3-2-1 rows; common berry radius and leaf above.\nReference: Lucide grape: repeated equal fruit circles organized as a bunch.\nReduction: Leaf and six grapes retained in a tapered bunch.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d395084-0155-47c6-a5ce-c8b1349a3045'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/muscatel_3d395084-0155-47c6-a5ce-c8b1349a3045.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'grape-bunch-leaf'
    keyshape = Keyshape.VRECT_L
    category = "objects"
    keywords = ('grape', 'bunch', 'leaf')

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

        # Three clear large berries replace six crowded small loops.
        circle('grape-left',16,28,8);circle('grape-right',32,28,8)
        path('grape-bottom',(16,36),[((32,36),8,8,False)])
        self.relate('connect','grape-left','grape-right')
        self.relate('connect','grape-bottom','grape-left');self.relate('connect','grape-bottom','grape-right')
        self.add_line('stem',(24,20),(24,12))
        self.relate('connect','stem','grape-left');self.relate('connect','stem','grape-right')
        self.add_bezier('leaf',(24,12),((24,4),(32,4),(40,4)),((40,10),(31,12),(24,12)))
        self.add_contour('leaf-outline','leaf',closed=True);self.relate('connect','stem','leaf-outline')
