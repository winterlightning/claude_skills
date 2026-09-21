# Final repair: Raise hood/bonnet to create8-unit body band.
'Side View Car with Open Hood\nPlan: Open-bottom car outline; equal wheels share body endpoints; raised hood remains distinct from roof.\nReference: Lucide car original and atomic-debug: one body silhouette with matched wheels.\nReduction: Drop window divisions; retain hood angle, cabin and two wheels.\nKeyshape: HRECT_M; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de4837e9-fc58-4000-be76-deb74b0a3723'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car hood release_de4837e9-fc58-4000-be76-deb74b0a3723.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'side-view-car-with-open-hood'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('side', 'view', 'car', 'with', 'open', 'hood')

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

        path('body',(4,24),[(4,16),(16,16),(24,10),(32,10),(40,16),(44,16),(44,24),(4,24)],True)
        for x in (12,36):circle(f'wheel-{x}',x,35,3)
        path('hood',(16,16),[(4,10)])
        self.relate('connect','hood','body')
