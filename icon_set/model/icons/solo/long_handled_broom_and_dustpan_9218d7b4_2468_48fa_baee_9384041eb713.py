'Long Handled Broom and Dustpan\nPlan: Broom at left and upright triangular dustpan at right; shared broom head/handle node.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Two bristle strokes retain the broom; plain triangular pan.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9218d7b4-2468-48fa-baee-9384041eb713'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/broom dustpan_9218d7b4-2468-48fa-baee-9384041eb713.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-handled-broom-and-dustpan'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('long', 'handled', 'broom', 'and', 'dustpan')

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

        self.add_line('handle',(6,6),(14,22))
        path('broom',(6,30),[((22,30),8,8,True),(22,38)])
        self.add_line('bristle-left',(6,30),(6,42));self.relate('connect','bristle-left','broom')
        self.relate('connect','handle','broom')
        self.add_polyline('pan',(42,6),(42,42),(32,42),(42,30))
