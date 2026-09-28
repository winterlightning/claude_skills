"""A disguised face: big round glasses over a nose and a bushy moustache (the disguise kit).

Symbol plan: symmetric about x = 24. Two r8 lens rings at (12, 16) and (36, 16) span the
full width, joined by a straight bridge from (20, 16) to (28, 16). The moustache is one
closed pad from y 32 to 40 whose top carries the nose as an r3 semicircular bump
(21, 32)-(27, 32) rising to (24, 29); its ends are r4 semicircles (x 13 and 35) around a
flat bottom. Pad top and bottom are 8 apart; the pad and nose stay 8+ from both lenses.
The reference's face circle is dropped: with an r20 rim every feature must fit inside
radius 12, where lenses shrink to dots and a closed moustache (8 tall) does not fit
(attempts/vA-*). The glasses-nose-moustache disguise carries the meaning on its own.
Lucide construction: 'glasses' (two round lenses and a bridge); rounded pad corners as in
Lucide's rounded rectangles.
Keyshape HRECT_L: centerline x 4..44 (lens sides), y 8..40 (lens tops, pad bottom).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f7b41792-3c8f-403e-b9a7-c16ae8fb7788"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__disguised-face/20260926T055140Z-thuan-mac/reference/disguised face old_f7b41792-3c8f-403e-b9a7-c16ae8fb7788.svg"
AUTHOR = "claude-opus-5-5"


class DisguisedFace(Solo48):
    icon_id = "disguised-face"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emoji"
    aliases = ("disguised face old", "incognito face", "disguise", "groucho glasses")
    keywords = ("disguise", "incognito", "glasses", "nose", "moustache", "mustache", "spy", "emoji", "face", "secret")

    def ring(self, name, cx, cy, r):
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        names = tuple(f"{name}-{q}" for q in ("nw", "ne", "se", "sw"))
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour(name, *names, closed=True)

    def build(self) -> None:
        lr, ly, dx = 8, 16, 12
        self.ring("lens-left", 24 - dx, ly, lr)
        self.ring("lens-right", 24 + dx, ly, lr)
        self.add_line("bridge", (24 - dx + lr, ly), (24 + dx - lr, ly))
        self.relate("connect", "lens-left", "bridge")
        self.relate("connect", "lens-right", "bridge")
        top, bot, xl, xr, nr = 32, 40, 17, 31, 3
        self.add_line("pad-top-left", (xl, top), (24 - nr, top))
        self.add_arc("nose", (24 - nr, top), (24 + nr, top), radius_x=nr)
        self.add_line("pad-top-right", (24 + nr, top), (xr, top))
        self.add_arc("pad-end-right", (xr, top), (xr, bot), radius_x=4)
        self.add_line("pad-bottom", (xr, bot), (xl, bot))
        self.add_arc("pad-end-left", (xl, bot), (xl, top), radius_x=4)
        self.add_contour("moustache", "pad-top-left", "nose", "pad-top-right", "pad-end-right",
                         "pad-bottom", "pad-end-left", closed=True)
