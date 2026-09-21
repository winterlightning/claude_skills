'Smoking Cigarette with Curl of Smoke\nPlan: Wide cigarette capsule with filter joint and a single flowing smoke curl.\nReference: Lucide cigarette original and atomic-debug: horizontal body and separated smoke.\nReduction: Remove multiple wisps; retain one curl and the filter division.\nKeyshape: HRECT_M; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a1155e0-7bcc-42cf-8cf2-d116d5369126'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/smoking_5a1155e0-7bcc-42cf-8cf2-d116d5369126.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smoking-cigarette-with-curl-of-smoke'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('smoking', 'cigarette', 'with', 'curl', 'of', 'smoke')

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

        self.add_polyline('cigarette',(4,30),(44,30),(44,38),(4,38),(4,30),closed=True)
        self.add_line('filter',(34,30),(34,38));self.relate('connect','filter','cigarette')
        path('smoke',(40,21),[((30,16),10,6,False),((24,10),6,6,True)])
