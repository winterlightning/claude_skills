'Church Steeple with Sloping Side Wings\nPlan: Spire and tall tower with lower wings; one arched opening.\nReference: Lucide church original and atomic-debug: repeated vertical structural axes.\nReduction: Reduce narrow window arch to one slot; retain spire and wings.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '585e8539-132b-43a8-b5b0-1e10b26ca71b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/steeple_585e8539-132b-43a8-b5b0-1e10b26ca71b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'church-steeple-with-sloping-side-wings'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('church', 'steeple', 'with', 'sloping', 'side', 'wings')

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

        self.add_polyline('tower',(16,44),(16,20),(24,4),(32,20),(32,44))
        self.add_polyline('wings',(16,28),(8,34),(8,44),(40,44),(40,34),(32,28))
        self.relate('connect','tower','wings')
        self.add_line('window',(24,26),(24,34))
