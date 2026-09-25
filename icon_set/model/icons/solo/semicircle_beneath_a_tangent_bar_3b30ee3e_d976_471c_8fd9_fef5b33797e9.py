'Semicircle Beneath a Tangent Bar\nPlan: Semicircular dome and tangent horizontal bar, with a shared crown node.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: HRECT_M; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b30ee3e-d976-471c-8fd9-fef5b33797e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astrology vulcan_3b30ee3e-d976-471c-8fd9-fef5b33797e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'semicircle-beneath-a-tangent-bar'
    keyshape = Keyshape.HRECT_M
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('semicircle', 'beneath', 'a', 'tangent', 'bar')

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

        path('dome',(4,38),[((24,10),20,28,True),((44,38),20,28,True),(4,38)],True)
        self.add_line('bar-left',(4,10),(24,10));self.add_line('bar-right',(24,10),(44,10))
        for s in ['left','right']:self.relate('connect',f'bar-{s}','dome')
        self.relate('connect','bar-left','bar-right')
