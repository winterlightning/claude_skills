'Extraterrestrial Alien Face.\nSymbol plan: Broad tapered alien head with two inward-slanting eye strokes. Tiny closed almond holes reduced to open slits. Rounded shoulder stroke sits4 ink units beneath the head.\nConstruction reference: No useful Lucide alien match. Source determines alien skull and eyes; human shoulder curves inform bust only.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '764d4882-3ab3-40e2-b064-eedc57ea1a69'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/alien 8bit_764d4882-3ab3-40e2-b064-eedc57ea1a69.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'alien-bust-almond-eyes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('alien', 'bust', 'almond', 'eyes')

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

        path('head',(10,18),[((24,4),14,14,True),((38,18),14,14,True),((24,34),14,16,True),((10,18),14,16,True)],True)
        self.add_line('left-eye',(19,17),(20,20))
        self.add_line('right-eye',(29,17),(28,20))
        path('shoulders',(8,44),[((24,42),16,2,True),((40,44),16,2,True)])
