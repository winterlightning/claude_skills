'Surprised Expression Face.\nPlan: Surprised face with inward-raised brows, tiny eyes and a vertical oval mouth.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Tiny pupil-like eyes remain dots; no facial part removed.\nKeyshape: CIRCLE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb5f5daa-9110-4900-a774-8d25f6235c98'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face frown open_bb5f5daa-9110-4900-a774-8d25f6235c98.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'surprised-face-with-tiny-eyes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('surprised', 'face', 'with', 'tiny', 'eyes')

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

        circle('face',24,24,20)
        self.add_line('brow-left',(16,16),(20,14));self.add_line('brow-right',(32,16),(28,14))
        for j,x in enumerate((15,33)):self.add_dot(f'eye-{j}',(x,24))
        ellipse('mouth',24,31,3,4)
