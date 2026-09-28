'Imperial Tie Fighter Spaceship.\n\nSymbol plan: Circular cockpit centered at (24,24), r9, short struts to two mirrored angled wings. Center window simplified to a dot. Extrema (6,6)-(42,42).\nConstruction reference: No useful exact Lucide match; ship-wheel supplies circular hub plus radial attachment principles.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ad9807b-be53-5585-8395-47cb15833c59'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-10/star wars_0ad9807b-be53-5585-8395-47cb15833c59.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'tie-fighter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('tie', 'fighter')

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

        path('cockpit',(15,24),[((24,15),9,9,True),((33,24),9,9,True),((24,33),9,9,True),((15,24),9,9,True)],True)
        self.add_dot('window',(24,24))
        for j,sgn in enumerate((-1,1)):
            x=24+sgn*18
            self.add_polyline(f'wing-{j}',(x-sgn*4,6),(x,12),(x,24),(x,36),(x-sgn*4,42))
            self.add_line(f'strut-{j}',(x,24),(24+sgn*9,24))
            self.relate('connect',f'wing-{j}',f'strut-{j}')
            self.relate('connect','cockpit',f'strut-{j}')
