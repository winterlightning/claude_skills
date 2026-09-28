"""A branched constellation: four stars of different sizes linked from a central star.

Symbol plan: stars are circles, links are straight lines that stop on the circles' rims.
The hub star (r6 about (20,22)) is four r6 arcs through its three link points
(5,-3), (3,5), (-5,3) and a top knot (-3,-5), all 5.83 from the centre, so neighbouring
links leave more than 8 apart. The largest star (r5) sits top-right, a small star (r4)
bottom-left and the smallest (r3) bottom-right, each link ending on the rim point facing
the hub.
Lucide construction: 'waypoints'/'share-2' - small circles joined by straight links that
end on the rims.
Keyshape SQUARE: centerline x 6..42 (small star left, large star right),
y 6..42 (large star top, bottom stars).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "568c70fd-77b9-53b1-a9a7-549b7795e05e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__branched-constellation/20260926T030905Z-thuan-mac/reference/astronomy constellation_568c70fd-77b9-53b1-a9a7-549b7795e05e.svg"
AUTHOR = "claude-opus-5-5"


class BranchedConstellation(Solo48):
    icon_id = "branched-constellation"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science/astronomy"
    aliases = ("astronomy-constellation", "constellation", "star-map")
    keywords = ("constellation", "stars", "astronomy", "sky", "night", "zodiac", "space", "star-chart")

    def _circle(self, name, a, b, r):
        self.add_arc(f"{name}-1", a, b, radius_x=r, sweep=True)
        self.add_arc(f"{name}-2", b, a, radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-1", f"{name}-2", closed=True)

    def build(self) -> None:
        hx, hy = 20, 22
        to_a, to_d, to_c, top = (hx + 5, hy - 3), (hx + 3, hy + 5), (hx - 5, hy + 3), (hx - 3, hy - 5)
        ring = [to_a, to_d, to_c, top]
        for i, p in enumerate(ring):
            self.add_arc(f"hub-{i + 1}", p, ring[(i + 1) % 4], radius_x=6, sweep=True)
        self.add_contour("hub", "hub-1", "hub-2", "hub-3", "hub-4", closed=True)
        # large star r5 at (37,11), small star r4 at (10,38), smallest r3 at (39,39)
        self._circle("star-large", (33, 14), (41, 8), 5)
        self._circle("star-small", (10, 34), (10, 42), 4)
        self._circle("star-tiny", (36, 39), (42, 39), 3)
        self.add_line("link-large", to_a, (33, 14))
        self.add_line("link-small", to_c, (10, 34))
        self.add_line("link-tiny", to_d, (36, 39))
        for link, star in (("link-large", "star-large"), ("link-small", "star-small"),
                           ("link-tiny", "star-tiny")):
            self.relate("connect", "hub", link)
            self.relate("connect", link, star)
