'Three Round Berries on a Leafy Stem\nPlan: Three berries in a triangular cluster, joined leafy stem; equal upper berry circles.\nReference: Lucide grape: equal circular fruit in a cluster.\nReduction: Three berries and one leaf retained; natural overlap requires opening review.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c09c4db6-f5a3-4264-8d21-6ab3263d70b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/berry_c09c4db6-f5a3-4264-8d21-6ab3263d70b9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-round-berries-on-a-leafy-stem'
    keyshape = Keyshape.VRECT_L
    category = "objects"
    keywords = ('three', 'round', 'berries', 'on', 'a', 'leafy', 'stem')

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

        circle('berry-left',16,28,8);circle('berry-right',32,28,8)
        path('berry-bottom',(16,36),[((32,36),8,8,False)])
        self.relate('connect','berry-left','berry-right');self.relate('connect','berry-left','berry-bottom');self.relate('connect','berry-right','berry-bottom')
        self.add_line('stem',(24,20),(24,12));self.relate('connect','stem','berry-left');self.relate('connect','stem','berry-right')
        self.add_bezier('leaf',(24,12),((24,4),(32,4),(40,4)),((40,10),(31,12),(24,12)))
        self.add_contour('leaf-outline','leaf',closed=True);self.relate('connect','stem','leaf-outline')
