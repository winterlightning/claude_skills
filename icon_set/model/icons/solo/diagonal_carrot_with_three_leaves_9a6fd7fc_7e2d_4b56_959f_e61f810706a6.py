# Final repair: Leaves attach to crown as a continuous fan; inspect internal openings.
'Diagonal Carrot with Three Leaves\nPlan: Diagonal root silhouette with three open leaf strokes sharing the crown.\nReference: Lucide carrot original and atomic-debug: diagonal taper and crown leaves.\nReduction: Drop internal root marks, use open leaf strokes to keep the crown legible.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a6fd7fc-7e2d-4b56-959f-e61f810706a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/cassava_9a6fd7fc-7e2d-4b56-959f-e61f810706a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-carrot-with-three-leaves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('diagonal', 'carrot', 'with', 'three', 'leaves')

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

        path('root',(6,42),[(16,18),((30,16),10,10,True),((32,30),10,10,True),(6,42)],True)
        for j,end in enumerate([(30,6),(42,6),(42,16)]):
            self.add_line(f'leaf-{j}',(30,16),end);self.relate('connect','root',f'leaf-{j}')
            for k in range(j):self.relate('connect',f'leaf-{j}',f'leaf-{k}')
