'Laughing Face with Smiling Eyes.\nPlan: Circular face radius20, mirrored eye arches and broad open grin with9x8 semicircular lower mouth. Mouth bottom35 leaves clear separation from face.\nReference: No useful Lucide exact laughing expression; standard coherent circle and semicircle construction.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c4724ad-76fb-4d54-83a8-1ee0219d47eb'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/face laugh beam_2c4724ad-76fb-4d54-83a8-1ee0219d47eb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'laughing-face-with-deep-open-grin'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('laughing', 'face', 'with', 'deep', 'open', 'grin')

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
        for j,x in enumerate((17,31)):path(f'eye-{j}',(x-2,17),[((x+2,17),2,2,True)])
        path('mouth',(15,27),[(33,27),((15,27),9,8,True)],True)
