'Lit Smoking Tobacco Cigarette.\nPlan: Diagonal cigarette with filter seam and detached smoke mark. Bounds6..42.\nConstruction reference: Lucide cigarette original and atomic-debug: narrow body, filter seam and detached smoke; source diagonal orientation.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '251e1919-65ab-4b80-b5b3-143b8f0f5187'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cigarette_251e1919-65ab-4b80-b5b3-143b8f0f5187.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lit-cigarette'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('lit', 'cigarette')

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

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        self.add_polyline('cigarette',(6,34),(26,14),(34,22),(14,42),closed=True)
        self.add_line('filter',(12,28),(20,36));self.relate('connect','cigarette','filter')
        self.add_line('smoke',(34,6),(42,14))
