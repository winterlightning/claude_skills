# Final repair: Compact cloud to exact square envelope; lower middle roof for spacing.
'Three Buildings beneath Cloud\nPlan: Three stepped buildings, pitched middle roof and upper-left cloud.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Drop windows to keep three buildings and cloud legible.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0291328f-6b9e-4cc3-80d5-84c234b92ad3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/building cloudy_0291328f-6b9e-4cc3-80d5-84c234b92ad3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-buildings-beneath-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('three', 'buildings', 'beneath', 'cloud')

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

        self.add_polyline('skyline',(6,42),(6,34),(18,34),(18,30),(26,24),(34,30),(34,6),(42,6),(42,42),(6,42),closed=True)
        self.add_line('join-low',(18,34),(18,42));self.add_line('join-high',(34,30),(34,42))
        self.relate('connect','join-low','skyline');self.relate('connect','join-high','skyline')
        path('cloud',(10,16),[((10,8),4,4,True),((21,8),6,2,True),((21,16),4,4,True),(10,16)],True)
