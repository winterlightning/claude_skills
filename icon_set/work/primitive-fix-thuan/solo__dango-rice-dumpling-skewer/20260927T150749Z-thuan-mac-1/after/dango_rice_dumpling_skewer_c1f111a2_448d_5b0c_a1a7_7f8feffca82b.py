"""Dango: three round rice dumplings threaded on a diagonal skewer.

Revision of the disapproved drawing, whose merged blobs read as a caterpillar.
Plan (VRECT_L, centerline (8,4)-(40,44)): three r5 circles tangent along the
(6,-8) direction, each pair sharing the exact 3-4-5 tangent point, and the stick
leaving the top dumpling at its far tangent point up to the top-right corner.
No useful Lucide subject match; circle-chain construction from `ellipsis`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c1f111a2-448d-5b0c-a1a7-7f8feffca82b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dango-rice-dumpling-skewer/20260927T150749Z-thuan-mac-1/reference/japanese sweets dango on stick_c1f111a2-448d-5b0c-a1a7-7f8feffca82b.svg"
AUTHOR = "claude-fable-5-1"


class DangoRiceDumplingSkewer(Solo48):
    icon_id = "dango-rice-dumpling-skewer"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("dango", "rice dumplings on a stick")
    keywords = ("dango", "rice", "dumpling", "skewer", "japanese", "sweets", "mochi")

    def build(self) -> None:
        centres = [(13, 39), (19, 31), (25, 23)]
        r = 5
        for i, (x, y) in enumerate(centres):
            lo = (x - 3, y + 4)   # tangent to the previous dumpling
            hi = (x + 3, y - 4)   # tangent to the next dumpling / stick
            self.add_arc(f"ball-{i}-a", hi, lo, radius_x=r)
            self.add_arc(f"ball-{i}-b", lo, hi, radius_x=r)
            self.add_contour(f"ball-{i}", f"ball-{i}-a", f"ball-{i}-b", closed=True)
        self.relate("connect", "ball-0", "ball-1")
        self.relate("connect", "ball-1", "ball-2")
        self.add_line("stick", (28, 19), (40, 4))
        self.relate("connect", "stick", "ball-2")
