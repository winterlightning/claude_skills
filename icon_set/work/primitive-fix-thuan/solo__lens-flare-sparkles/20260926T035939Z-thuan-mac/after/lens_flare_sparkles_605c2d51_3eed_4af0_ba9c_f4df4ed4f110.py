"""Photo lens flares: two flare rings with four spikes each and two small plus sparkles.

Symbol plan: point-symmetric about (24,24). Each flare is an open r5 ring with four spikes
leaving its cardinal points (4 beyond the rim), at the top-left (15,15) and the
bottom-right (33,33). Each sparkle is a plus with arms of 4 tucked into the top-right
(37,11) and bottom-left (11,37) corners, 9.8 clear of the flare spikes.
Lucide construction: 'sparkles' / 'sun' - rings with short straight rays and small
plus glints.
Keyshape SQUARE: centerline x 6..42, y 6..42 (outer flare spikes).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "605c2d51-3eed-4af0-ba9c-f4df4ed4f110"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__lens-flare-sparkles/20260926T035939Z-thuan-mac/reference/photo flares_605c2d51-3eed-4af0-ba9c-f4df4ed4f110.svg"
AUTHOR = "claude-opus-5-5"


class LensFlareSparkles(Solo48):
    icon_id = "lens-flare-sparkles"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography/effects"
    aliases = ("photo-flares", "lens-flare", "flares")
    keywords = ("flare", "lens", "sparkle", "light", "glare", "photo", "effect", "shine", "glint")

    def build(self) -> None:
        for name, (cx, cy) in (("flare-a", (15, 15)), ("flare-b", (33, 33))):
            n, e, s, w = (cx, cy - 5), (cx + 5, cy), (cx, cy + 5), (cx - 5, cy)
            self.add_arc(f"{name}-ne", n, e, radius_x=5, sweep=True)
            self.add_arc(f"{name}-se", e, s, radius_x=5, sweep=True)
            self.add_arc(f"{name}-sw", s, w, radius_x=5, sweep=True)
            self.add_arc(f"{name}-nw", w, n, radius_x=5, sweep=True)
            self.add_contour(f"{name}-ring", f"{name}-ne", f"{name}-se", f"{name}-sw", f"{name}-nw", closed=True)
            for sname, a, b in (("n", n, (cx, cy - 9)), ("e", e, (cx + 9, cy)),
                                ("s", s, (cx, cy + 9)), ("w", w, (cx - 9, cy))):
                self.add_line(f"{name}-spike-{sname}", a, b)
                self.relate("connect", f"{name}-ring", f"{name}-spike-{sname}")
        for name, (cx, cy) in (("sparkle-a", (37, 11)), ("sparkle-b", (11, 37))):
            self.add_line(f"{name}-h", (cx - 4, cy), (cx + 4, cy))
            self.add_line(f"{name}-v", (cx, cy - 4), (cx, cy + 4))
            self.relate("connect", f"{name}-h", f"{name}-v")
