'Square Candy with Dripping Glaze\nPlan: Rounded candy slab; glaze is a continuous wave attached at side nodes.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Reduce many small drips to two broad lobes, retaining the coated candy slab.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad8999b0-bfbe-484f-b448-4098df37f92d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/caramel_ad8999b0-bfbe-484f-b448-4098df37f92d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-candy-with-dripping-glaze'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('square', 'candy', 'with', 'dripping', 'glaze')

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

        path('body',(6,18),[(6,10),((10,6),4,4,True),(38,6),((42,10),4,4,True),(42,26),(42,38),((38,42),4,4,True),(10,42),((6,38),4,4,True),(6,18)],True)
        path('glaze',(6,18),[((18,18),6,6,False),((30,18),6,10,False),((42,26),12,8,False)])
        self.relate('connect','glaze','body')
