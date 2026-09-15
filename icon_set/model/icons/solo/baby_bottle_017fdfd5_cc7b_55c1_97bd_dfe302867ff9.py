"""Give the feeding teat a clear, taller profile and a consistent collar band.
Plan: symmetric bottle body, collar with 8-unit band, curved nipple.
VRECT_L centerline extremes (8,4)-(40,44).
Lucide: milk; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '017fdfd5-cc7b-55c1-97bd-dfe302867ff9'
SOURCE_PATH = 'pictographic-primitives/babies/baby care bottle_017fdfd5-cc7b-55c1-97bd-dfe302867ff9.svg'
AUTHOR = 'gpt-6'

class BabyBottle(Solo48):
    icon_id = 'baby-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/baby-care'
    aliases = ()
    keywords = ('bottle', 'baby', 'milk', 'feeding', 'teat', 'infant', 'formula', 'nursing')

    def build(self):

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, (kind, end, *args) in enumerate(commands):
                name = f'{n}-{j}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)

        def circle(n, x, y, r):
            path(n, (x - r, y), [('A', (x, y - r), r, r, True), ('A', (x + r, y), r, r, True), ('A', (x, y + r), r, r, True), ('A', (x - r, y), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        # Full-height teat dome and split rim nodes avoid the shallow collar pocket.
        path('body',(8,22),[('L',(8,36)),('A',(16,44),8,8,False),('L',(32,44)),('A',(40,36),8,8,False),('L',(40,22))])
        poly('collar',(8,22),(8,14),(14,14),(34,14),(40,14),(40,22),(8,22))
        path('teat',(14,14),[('A',(24,4),10,10,True),('A',(34,14),10,10,True)])
        join('body','collar');join('teat','collar')
