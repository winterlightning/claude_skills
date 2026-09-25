'Plain Three-Layer Hamburger\nPlan: Three broad burger layers; shared horizontal seams avoid overlapping capsule outlines.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Keep domed bun and two clear horizontal seams; omit all garnish.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cbb84b4-db71-4fad-9fac-a1f7112ead64'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/patty_7cbb84b4-db71-4fad-9fac-a1f7112ead64.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-three-layer-hamburger'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('plain', 'three', 'layer', 'hamburger')

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

        path('outline',(4,24),[((44,24),20,16,True),(44,32),((36,40),8,8,True),(12,40),((4,32),8,8,True),(4,24)],True)
        for y in (24,32):
            self.add_line(f'seam-{y}',(4,y),(44,y));self.relate('connect',f'seam-{y}','outline')
