# Final repair: Lower roof under cross and retain arch doorway.
'Small Church with Roof Cross\nPlan: Symmetric chapel gable with roof cross and central arch doorway.\nReference: Lucide church original and atomic-debug: gable and arched entrance.\nReduction: Remove eave overhangs; preserve chapel, cross and doorway.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca26c7b2-87d4-487a-9777-124368d5e15b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/chapel_ca26c7b2-87d4-487a-9777-124368d5e15b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'small-church-with-roof-cross'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('small', 'church', 'with', 'roof', 'cross')

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

        self.add_polyline('house',(6,42),(6,26),(24,18),(42,26),(42,42),(6,42))
        self.add_line('cross-v',(24,6),(24,18));self.add_line('cross-h',(18,10),(30,10));self.relate('connect','cross-h','cross-v');self.relate('connect','cross-v','house')
        path('door',(18,42),[(18,34),((30,34),6,6,True),(30,42)])
        self.relate('connect','door','house')
