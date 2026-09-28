"""A smiling oval face sits beneath two large symmetrical lobes that sweep outward and hang down beside the cheeks. A circular ornament rests at the forehead, with short angular lines rising from the temples.

HRECT_XL visible bounds (2,6)-(46,42); central smiling face, paired hanging lobes and forehead ornament. Eyes and temple marks omitted. No useful exact Lucide match; mirrored lobe dimensions and shared ornament attachments.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1cbfd2f8-04d6-4b91-b205-3ee8299e6715'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__alien-head-twin-hanging-lobes/20260926T064521Z-thuan-mac/reference/lethan lutian_1cbfd2f8-04d6-4b91-b205-3ee8299e6715.svg'
AUTHOR = "claude-opus-5-5"

class AlienHeadTwinHangingLobes(Solo48):
    icon_id = 'alien-head-twin-hanging-lobes'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('twilek', 'alien', 'head', 'headdress', 'face', 'fiction')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        """Revision attempt per review: rounded lobe bottoms (r4 semicircles), inward-curving
        inner lobe lines, a complete r12 face circle hanging beneath a larger open r5 bun, two
        small curved eyes and a separate smile. The face cannot hold its features: with lobes
        at least 8 wide on each side the face is at most 24 wide (r12), but two eyes 8 apart and
        8 inside the outline plus a smile 8 below them need a face about 32 wide. The
        validator reports the eye and smile clearance failures (validation.txt)."""
        # bun and face
        self.circle('bun', 24, 11, 5)
        self.add_arc('face-left', (24, 16), (24, 40), radius_x=12, sweep=False)
        self.add_arc('face-right', (24, 40), (24, 16), radius_x=12, sweep=False)
        self.add_contour('face', 'face-left', 'face-right', closed=True)
        self.relate('connect', 'bun', 'face')
        # lobes: outer arch from the bun, rounded bottom, inward-curving inner line
        for side, m in (('left', 1), ('right', -1)):
            x = lambda v: 24 - m * (24 - v)
            self.add_arc(f'{side}-arch', (x(19), 11), (x(4), 26), radius_x=15, sweep=(m == -1))
            self.add_line(f'{side}-outer', (x(4), 26), (x(4), 36))
            self.add_arc(f'{side}-bottom', (x(4), 36), (x(12), 36), radius_x=4, sweep=(m == -1))
            self.add_arc(f'{side}-inner', (x(12), 36), (x(8), 20), radius_x=16, sweep=(m == 1))
            self.add_contour(f'lobe-{side}', f'{side}-arch', f'{side}-outer', f'{side}-bottom', f'{side}-inner')
            self.relate('connect', 'bun', f'lobe-{side}')
        # eyes and smile
        self.add_arc('eye-left', (18, 27), (22, 27), radius_x=3)
        self.add_arc('eye-right', (26, 27), (30, 27), radius_x=3)
        self.add_arc('smile', (20, 33), (28, 33), radius_x=5, sweep=False)
