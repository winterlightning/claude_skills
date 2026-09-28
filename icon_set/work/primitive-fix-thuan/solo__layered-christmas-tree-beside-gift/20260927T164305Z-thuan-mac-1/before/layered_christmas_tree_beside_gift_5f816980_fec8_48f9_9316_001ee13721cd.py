# Final repair: Use one broad conical tree silhouette to eliminate narrow tier junctions.
'Layered Christmas Tree beside Gift\nPlan: Layered tree at left and tied present right form a holiday scene.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Two branch tiers and one bow stroke replace fine tiers/ribbons; preserve scene.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f816980-fec8-48f9-9316-001ee13721cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/christmas tree ornaments gift_5f816980-fec8-48f9-9316-001ee13721cd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'layered-christmas-tree-beside-gift'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('layered', 'christmas', 'tree', 'beside', 'gift')

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

        self.add_polyline('tree',(16,6),(6,34),(26,34),(16,6),closed=True)
        self.add_line('trunk',(16,34),(16,42));self.relate('connect','trunk','tree')
        box('gift',34,34,42,42,2)
        self.add_polyline('bow',(34,26),(38,34),(42,26));self.relate('connect','bow','gift')
