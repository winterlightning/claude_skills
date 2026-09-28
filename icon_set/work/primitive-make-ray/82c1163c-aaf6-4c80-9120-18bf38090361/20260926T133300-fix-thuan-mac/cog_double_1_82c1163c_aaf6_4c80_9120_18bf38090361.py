"""Two cogs on a rising diagonal.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: each cog is a hub ring (r5) with seven radial teeth reaching r10,
built on the ring's integer points (cardinal and 3-4-5 directions), as in
Lucide `cog` (rim ring plus radial tooth strokes). The upper-right cog sits at
(32,16) and the lower-left one is its point reflection through (24,24), so
the pair has 180-degree symmetry. Each cog leaves its tooth gap facing the
other cog (where gears mesh), which keeps every part 8+ apart.
Revision: the earlier four-tooth octagon outlines read as blobs; radial teeth
around an open hub now read as gears.
Reduction: eight teeth per gear become seven (the eighth would face the other
gear within 8 units); the separate inner hub circle is the ring's opening.
Construction reference: Lucide `cog`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '82c1163c-aaf6-4c80-9120-18bf38090361'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cog-double-1/20260926T125429Z-thuan-mac/reference/cog double 1_82c1163c-aaf6-4c80-9120-18bf38090361.svg'
AUTHOR = "claude-opus-5-5"

RING_R = 5
TOOTH_SCALE = 2           # tooth tips at 2 x the ring point: radius 10
UPPER = (32, 16)
# tooth directions for the upper-right cog, as ring offsets of length 5, in
# clockwise (screen) order; the gap at 90-180 degrees faces the other cog
TEETH = [(5, 0), (3, 4), (0, 5), (-5, 0), (-4, -3), (0, -5), (4, -3)]


class Drawing(Solo48):
    icon_id = 'cog-double-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('gears', 'cogs', 'settings')
    keywords = ('cog', 'double', 'gear', 'gears', 'settings', 'mechanism')

    def cog(self, name, c, teeth):
        cx, cy = c
        bases = [(cx + dx, cy + dy) for dx, dy in teeth]
        n = len(bases)
        for i in range(n):
            self.add_arc(f'{name}-rim-{i}', bases[i], bases[(i + 1) % n], radius_x=RING_R, sweep=True)
        self.add_contour(f'{name}-rim', *(f'{name}-rim-{i}' for i in range(n)), closed=True)
        for i, (dx, dy) in enumerate(teeth):
            tip = (cx + TOOTH_SCALE * dx, cy + TOOTH_SCALE * dy)
            self.add_line(f'{name}-tooth-{i}', bases[i], tip)
            self.relate('connect', f'{name}-tooth-{i}', f'{name}-rim-{i}')
            self.relate('connect', f'{name}-tooth-{i}', f'{name}-rim-{(i - 1) % n}')

    def build(self):
        self.cog('cog-upper', UPPER, TEETH)
        self.cog('cog-lower', (48 - UPPER[0], 48 - UPPER[1]), [(-dx, -dy) for dx, dy in TEETH])
