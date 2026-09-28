"""A smiling face wearing dark sunglasses.

Plan: CIRCLE. Face: r20 circle of four quarter arcs about (24,24). Sunglasses: a frame bar from (14,18) to (34,18) split where two r3 lens rings hang from it, centred (17,21) and (31,21); r3 rings paint as near-solid discs, so they read as dark lenses. Smile: an r6 arc from (19,32) to (29,32) under the lenses.
Review of the rejected drawing: the lenses were shallow open cups hanging from a bar across the rim, which read as drooping sad eyes or a mask; the original has two dark rounded lenses on a bridge with a smile below.
Omissions: the temples reaching the rim (no lattice points on the r20 rim at lens height) and the bridge gap between the lenses.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6b207644-924b-4415-9162-5bfe9adfd9bf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-face-wearing-sunglasses/20260928T042731Z-thuan-mac-1/reference/face sunglasses_6b207644-924b-4415-9162-5bfe9adfd9bf.svg'
AUTHOR = 'claude-fable-5-1'


class SmilingFaceWearingSunglasses(Solo48):
    icon_id = 'smiling-face-wearing-sunglasses'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('cool-face', 'face-with-sunglasses')
    keywords = ('face', 'sunglasses', 'cool', 'smiling', 'emoji', 'shades')

    def build(self) -> None:
        def circle(name, cx, cy, r):
            pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
            for i in range(4):
                self.add_arc(f'{name}-{i}', pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
            self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)
        circle('face', 24, 24, 20)
        circle('lens-left', 17, 21, 3)
        circle('lens-right', 31, 21, 3)
        self.add_line('frame-left', (14, 18), (17, 18))
        self.add_line('bridge', (17, 18), (31, 18))
        self.add_line('frame-right', (31, 18), (34, 18))
        for a, b in (('frame-left', 'lens-left'), ('bridge', 'lens-left'), ('bridge', 'lens-right'),
                     ('frame-right', 'lens-right'), ('frame-left', 'bridge'), ('bridge', 'frame-right')):
            self.relate('connect', a, b)
        self.add_arc('smile', (19, 32), (29, 32), radius_x=6, sweep=False)
