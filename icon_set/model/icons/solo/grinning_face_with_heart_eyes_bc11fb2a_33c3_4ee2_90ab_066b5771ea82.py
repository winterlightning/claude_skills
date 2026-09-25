'Smiling Face With Heart Eyes.\nPlan: Round face, paired solid heart marks reduced to two round-ended strokes meeting at a point, and open grin. No tiny enclosed eye holes.\nReference: Lucide heart: paired lobes and converging lower sides, reduced to solid marks for48px.\nKeyshape: CIRCLE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc11fb2a-33c3-4ee2-90ab-066b5771ea82'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/face grin hearts_bc11fb2a-33c3-4ee2-90ab-066b5771ea82.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'grinning-face-with-heart-eyes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('grinning', 'face', 'with', 'heart', 'eyes')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
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

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        circle('face',24,24,20)
        for j,x in enumerate((17,31)):self.add_polyline(f'heart-eye-{j}',(x-2,17),(x,20),(x+2,17))
        path('mouth',(15,29),[(33,29),((15,29),9,6,True)],True)
