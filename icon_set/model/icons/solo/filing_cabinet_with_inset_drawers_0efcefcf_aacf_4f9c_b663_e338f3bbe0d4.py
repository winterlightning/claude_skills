'Two Drawer Filing Cabinet.\nPlan: Rounded filing cabinet with two drawers and centered horizontal handles.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Inset drawer borders reduced to one shared dividing seam; two drawer handles retained.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0efcefcf-aacf-4f9c-b663-e338f3bbe0d4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/file cabinet_0efcefcf-aacf-4f9c-b663-e338f3bbe0d4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'filing-cabinet-with-inset-drawers'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('filing', 'cabinet', 'with', 'inset', 'drawers')

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

        box('body',8,4,40,44,4)
        self.add_line('divider',(8,24),(40,24));self.relate('connect','divider','body')
        for y in (14,34):self.add_line(f'handle-{y}',(20,y),(28,y))

SOURCE_REFERENCES = [('82d48897-9f8c-4b4a-8bf3-9bf4db329294', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/file cabinet_82d48897-9f8c-4b4a-8bf3-9bf4db329294.svg')]
