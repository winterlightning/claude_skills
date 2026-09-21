'Big Cat Head in Profile\nPlan: Open neck and curved feline profile; ear, projecting muzzle and tear mark remain.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Remove small nose loop; retain blunt muzzle, ear and cheek marking.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad19cb98-f7e5-468d-b030-7a06c12b6802'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cheetah_ad19cb98-f7e5-468d-b030-7a06c12b6802.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'big-cat-head-in-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('big', 'cat', 'head', 'in', 'profile')

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

        path('profile',(30,42),[((20,32),10,10,False),(14,32),((6,24),8,8,True),(12,20),(18,10),(28,10),(34,6),((42,14),8,8,True),(42,24)])
        self.add_line('tear',(24,19),(23,22))
