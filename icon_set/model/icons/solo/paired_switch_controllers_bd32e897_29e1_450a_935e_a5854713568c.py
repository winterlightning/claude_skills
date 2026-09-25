'Switch Game Controllers.\nPlan: Two upright controller halves with straight inner edges and broadly rounded outer corners. No buttons in reference. Bounds6..42.\nReference: Lucide gamepad-2: smooth controller corners; source empty paired halves retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd32e897-29e1-450a-935e-a5854713568c'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-11/switch joy control_bd32e897-29e1-450a-935e-a5854713568c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-switch-controllers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('paired', 'switch', 'controllers')

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

        for j,flip in enumerate((False,True)):
         def pt(x,y):return (48-x,y) if flip else (x,y)
         path(f'controller-{j}',pt(19,6),[pt(14,6),(pt(6,14),8,8,flip),pt(6,34),(pt(14,42),8,8,flip),pt(19,42),pt(19,6)],True)
