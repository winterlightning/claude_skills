'Unimpressed Expression Face.\nPlan: Circular face, flat paired eyes and a shallow frown. Radius20 radial envelope.\nReference: No useful exact Lucide emotion match; circular face and sparse expression from source.\nKeyshape: CIRCLE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38ba1d1f-eaf7-4ce3-9724-9f6ee04cc5ef'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/face unamused_38ba1d1f-eaf7-4ce3-9724-9f6ee04cc5ef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'unimpressed-face-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('unimpressed', 'face', 'solo')

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
        self.add_line('eye-left',(14,19),(18,19));self.add_line('eye-right',(30,19),(34,19))
        path('frown',(19,33),[((29,33),5,3,True)])
