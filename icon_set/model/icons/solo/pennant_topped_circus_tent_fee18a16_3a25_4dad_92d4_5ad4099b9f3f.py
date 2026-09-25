# Final repair: Lengthen flagpole to leave legal space above roof; lower door with tent.
'Pennant Topped Circus Tent\nPlan: Circus tent gable with peak pennant, straight walls and arched doorway.\nReference: Lucide tent original and atomic-debug: broad triangular silhouette.\nReduction: Drop small scallops; retain pennant and arched entrance.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fee18a16-3a25-4dad-92d4-5ad4099b9f3f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/circus tents_fee18a16-3a25-4dad-92d4-5ad4099b9f3f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pennant-topped-circus-tent'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('pennant', 'topped', 'circus', 'tent')

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

        self.add_polyline('tent',(6,42),(6,30),(24,22),(42,30),(42,42),(6,42))
        self.add_polyline('flag',(24,22),(24,6),(36,6),(36,14),(24,14));self.relate('connect','flag','tent')
        path('door',(18,42),[(18,38),((30,38),6,6,True),(30,42)])
        self.relate('connect','door','tent')
