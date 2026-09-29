'Face with Head Bandage.\n\nSymbol plan: Round head and two broad diagonal wrap edges. Extra short wrap seam omitted.\nConstruction reference: human_ref/user.svg: circular head; bandage is intrinsic wrapping, not a modifier.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5d36fda-d12e-4a2d-a970-b3258b3fc57c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/face head bandage_e5d36fda-d12e-4a2d-a970-b3258b3fc57c.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'head-wrapped-in-bandage'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('head', 'wrapped', 'in', 'bandage')

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

        path('head',(4,24),[((24,4),20,20,True),((40,12),20,20,True),((44,24),20,20,True),((24,44),20,20,True),((4,24),20,20,True)],True)
        self.add_line('wrap-upper',(4,24),(40,12))
        self.add_line('wrap-lower',(12,40),(44,24))
        self.relate('connect','head','wrap-upper')
        self.relate('connect','head','wrap-lower')
