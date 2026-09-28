'Round Bodied Hen\nPlan: Hen body with upright head and tail; two equal attached leg strokes.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Remove eye, crest layering and wattle; silhouette retains beak, neck and tail.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9555863c-04f0-4a1d-97a0-34f34e0a22f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/broiler_9555863c-04f0-4a1d-97a0-34f34e0a22f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-bodied-hen'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('round', 'bodied', 'hen')

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

        path('hen',(6,14),[(14,22),(26,22),(26,14),((38,14),6,8,True),(42,18),(38,22),(38,26),((22,36),16,10,True),((6,26),16,10,True),(6,14)],True)
        self.add_polyline('legs',(16,42),(22,36),(28,42));self.relate('connect','hen','legs')
