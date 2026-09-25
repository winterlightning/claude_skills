'Venetian Gondola Boat.\nPlan: Long shallow hull with raised curved ends and an oblique oar. Bounds4,8..44,40.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Retain right raised prow and oar; omit tiny prow teeth.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90252eb4-ab81-4240-8b07-60946ef03910'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gondola_90252eb4-ab81-4240-8b07-60946ef03910.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gondola-with-oar'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('gondola', 'with', 'oar')

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

        path('hull',(4,14),[(4,24),((16,36),12,12,False),(32,36),((44,24),12,12,False),(44,8)])
        self.add_line('rim',(4,24),(44,24));self.relate('connect','rim','hull')
        self.add_line('oar',(16,40),(34,22));self.relate('connect','oar','rim');self.relate('connect','oar','hull')
