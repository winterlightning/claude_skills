'Top and Bottom Text Wrap.\nPlan: Central rounded object between two pairs of abstract text lines.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Vertical layout expanded within SOLO48 to retain all four text lines and the object opening.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'afafd268-1d4a-497d-a13e-3b63846deb97'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/jump object_afafd268-1d4a-497d-a13e-3b63846deb97.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'object-between-text-lines'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('object', 'between', 'text', 'lines')

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

        for y in (4,12,36,44):self.add_line(f'text-{y}',(8,y),(40,y))
        box('object',16,20,32,28,2)

SOURCE_REFERENCES = [('ea79e3d0-8480-4a7b-b338-7cecdce62cec', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/jump to next column_ea79e3d0-8480-4a7b-b338-7cecdce62cec.svg')]
