'Domed Bubble Tea Cup\nPlan: Tapered cup with half-ellipse lid, attached bent straw, and two boba pearls.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Two pearls replace three to preserve spacing in the taper.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '273a7915-a08f-4e47-b937-2520d716f214'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bubble tea shake_273a7915-a08f-4e47-b937-2520d716f214.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'domed-bubble-tea-cup'
    keyshape = Keyshape.VRECT_L
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('domed', 'bubble', 'tea', 'cup')

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

        path('cup',(8,20),[(13,44),(35,44),(40,20),(8,20)],True)
        path('lid',(8,20),[((40,20),16,10,True)])
        self.relate('connect','lid','cup')
        self.add_polyline('straw',(24,10),(24,4));self.relate('connect','straw','lid')
        circle('pearl',24,33,3)
