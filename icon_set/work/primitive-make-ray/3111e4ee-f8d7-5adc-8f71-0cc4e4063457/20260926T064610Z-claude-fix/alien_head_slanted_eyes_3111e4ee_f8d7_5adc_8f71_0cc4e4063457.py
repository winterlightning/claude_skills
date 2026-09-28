"""Replace the pointed lower jaw with a true horizontal oval while retaining the eye style. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3111e4ee-f8d7-5adc-8f71-0cc4e4063457'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__alien-head-slanted-eyes/20260926T064521Z-thuan-mac/reference/alien_3111e4ee-f8d7-5adc-8f71-0cc4e4063457.svg'
AUTHOR = "claude-opus-5-5"

class AlienHeadSlantedEyes(Solo48):
    icon_id = 'alien-head-slanted-eyes'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('alien', 'head', 'face', 'extraterrestrial', 'eyes', 'space')

    def circle(self, name, x, y, r):
        points = [(x - r, y), (x, y - r), (x + r, y), (x, y + r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i + 1) % 4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        """Revision attempt per review: a taller, narrower head (VRECT_L) with a broad r16
        rounded forehead about (24, 20) and sides that taper in two cubics to a rounded chin
        (24, 44); two large closed almond eyes (two r7 arcs on a (12, 6) chord, 10 across,
        empty inside), mirrored and rising toward the outer corners. The eyes cannot keep the
        SOLO48 8-unit clearance: two such eyes need about 2 x 11 + 8 between them + 2 x 8 to
        the head = 46 units of width, and a head taller than wide is 32 wide at most. The
        validator reports the eye/head and eye/eye clearance failures (validation.txt)."""
        self.add_arc('forehead-left', (8, 20), (24, 4), radius_x=16)
        self.add_arc('forehead-right', (24, 4), (40, 20), radius_x=16)
        self.add_bezier('cheek-right', (40, 20), ((40, 32), (30, 44), (24, 44)))
        self.add_bezier('cheek-left', (24, 44), ((18, 44), (8, 32), (8, 20)))
        self.add_contour('head', 'forehead-left', 'forehead-right', 'cheek-right', 'cheek-left', closed=True)
        for side, inner, outer in (('left', (20, 28), (8, 22)), ('right', (28, 28), (40, 22))):
            up = side == 'left'
            self.add_arc(f'eye-{side}-upper', inner, outer, radius_x=7, sweep=not up)
            self.add_arc(f'eye-{side}-lower', outer, inner, radius_x=7, sweep=not up)
            self.add_contour(f'eye-{side}', f'eye-{side}-upper', f'eye-{side}-lower', closed=True)
