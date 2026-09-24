'Surgical Scalpel Making a Cut.\nPlan: Diagonal scalpel points toward an incision between two separated surface strokes.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Small bevel detail removed; rounded handle, curved blade and incision gap retained.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8386e8f-cf90-460c-9bbf-04c34adf60e1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/incision_b8386e8f-cf90-460c-9bbf-04c34adf60e1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'scalpel-making-incision'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('scalpel', 'making', 'incision')

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

        path('scalpel',(14,32),[(32,6),(38,6),((42,12),4,6,True),(26,28),((14,32),16,8,True)],True)
        self.add_line('blade-joint',(24,17),(32,22));self.relate('connect','blade-joint','scalpel')
        self.add_line('surface-left',(6,42),(12,42));self.add_line('surface-right',(24,42),(42,42))
