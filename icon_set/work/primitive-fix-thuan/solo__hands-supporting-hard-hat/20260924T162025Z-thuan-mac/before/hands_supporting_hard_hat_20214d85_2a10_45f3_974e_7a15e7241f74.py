'Hands Protecting Safety Helmet.\n\nSymbol plan: Domed helmet and brim above mirrored cupped hand strokes. Crown rib and cuff details omitted to preserve spacing.\nConstruction reference: Lucide hard-hat: dome and broad brim; human_ref/user.svg informs rounded human construction.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20214d85-2a10-45f3-974e-7a15e7241f74'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/labor hands action_20214d85-2a10-45f3-974e-7a15e7241f74.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'hands-supporting-hard-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('hands', 'supporting', 'hard', 'hat')

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

        path('helmet',(14,22),[((24,6),10,16,True),((34,22),10,16,True)])
        self.add_polyline('brim',(10,22),(14,22),(34,22),(38,22))
        self.relate('connect','helmet','brim')
        for j,sgn in enumerate((-1,1)):
            x=24+sgn*18; inner=24+sgn*7
            path(f'hand-{j}',(x,30),[(x,34),((inner,42),11,8,sgn<0)])
