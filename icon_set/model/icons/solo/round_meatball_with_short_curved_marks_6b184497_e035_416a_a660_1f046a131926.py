'Round Meatball with Short Curved Marks\nPlan: Circular meatball with four isolated short surface marks derived in quadrants.\nReference: Lucide cookie original and atomic-debug: large circular outline and sparse texture.\nReduction: Short broad marks replace small curves; preserve four surface marks.\nKeyshape: CIRCLE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b184497-e035-416a-a660-1f046a131926'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/meatball_6b184497-e035-416a-a660-1f046a131926.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-meatball-with-short-curved-marks'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('round', 'meatball', 'with', 'short', 'curved', 'marks')

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

        circle('ball',24,24,20)
        for j,(x,y) in enumerate([(18,16),(32,20),(28,32),(16,28)]):
            self.add_line(f'mark-{j}',(x-1,y),(x+1,y))
