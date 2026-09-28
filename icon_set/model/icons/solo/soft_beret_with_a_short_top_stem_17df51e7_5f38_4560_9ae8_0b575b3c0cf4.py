'Soft Beret with a Short Top Stem\nPlan: Asymmetric soft beret crown and broad headband; short top stem.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Broad crown retains directional softness; widen headband to legal spacing.\nKeyshape: HRECT_M; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17df51e7-5f38-4560-9ae8-0b575b3c0cf4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beret_17df51e7-5f38-4560-9ae8-0b575b3c0cf4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'soft-beret-with-a-short-top-stem'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('soft', 'beret', 'with', 'a', 'short', 'top', 'stem')

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

        path('crown',(4,30),[((24,14),20,16,True),((44,26),20,12,True),((36,30),8,4,True),(12,30),((4,30),4,4,True)],True)
        self.add_polyline('band',(12,30),(12,38),(36,38),(36,30));self.relate('connect','band','crown')
        self.add_line('stem',(24,10),(24,14));self.relate('connect','stem','crown')
