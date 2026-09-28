"""A cocker spaniel face: a domed head with long floppy ears hanging on both sides, a nose and jowls.

Symbol plan: symmetric about x=24. The outline is one open run: each ear's outer edge
rises from the ear's foot to a branch node on the head, and the dome arches over between
the two nodes. From each node the ear's inner edge falls to the jowl corner, and the
ear's foot curls in to the same corner, so each ear is a long closed lobe. The muzzle:
a small ring nose (r2, approved 4-diameter circle), a short mouth line below it, and two
jowl curves from the mouth to the jowl corners. All joins are shared endpoints; the nose
is 9 from the ears' inner edges.
The reference has no eyes; none are added.
Lucide construction: 'dog' - dome head with hanging ears and a nose/mouth muzzle.
Keyshape HRECT_L: centerline x 4..44 (ear feet), y 8..40 (dome top, ear feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6d412e40-a1ee-5f45-85b5-a8eac4b50e9e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__cocker-spaniel-face/20260926T044250Z-thuan-mac/reference/cocker spaniel_6d412e40-a1ee-5f45-85b5-a8eac4b50e9e.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    return (48 - p[0], p[1])


class CockerSpanielFace(Solo48):
    icon_id = "cocker-spaniel-face"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/pets"
    aliases = ("cocker spaniel", "spaniel", "dog face")
    keywords = ("dog", "cocker spaniel", "spaniel", "puppy", "pet", "ears", "animal", "breed")

    def build(self) -> None:
        node, apex, foot, corner = (11, 16), (24, 8), (4, 40), (13, 36)
        # outline: left ear outer edge, dome, right ear outer edge
        self.add_bezier("ear-outer-l", foot, ((4, 28), (8, 20), node))
        self.add_bezier("dome-l", node, ((13, 11), (18, 8), apex))
        self.add_bezier("dome-r", apex, (_m((18, 8)), _m((13, 11)), _m(node)))
        self.add_bezier("ear-outer-r", _m(node), (_m((8, 20)), _m((4, 28)), _m(foot)))
        self.add_contour("outline", "ear-outer-l", "dome-l", "dome-r", "ear-outer-r")
        # nose and mouth
        nx, ny, nr = 24, 26, 2
        pts = [(nx - nr, ny), (nx, ny - nr), (nx + nr, ny), (nx, ny + nr)]
        names = ("nose-nw", "nose-ne", "nose-se", "nose-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=nr)
        self.add_contour("nose", *names, closed=True)
        mouth_end = (24, 32)
        self.add_line("mouth", (nx, ny + nr), mouth_end)
        self.relate("connect", "nose", "mouth")
        for side, f in (("l", lambda p: p), ("r", _m)):
            self.add_bezier(f"ear-inner-{side}", f(node), (f((13, 22)), f((13, 30)), f(corner)))
            self.add_bezier(f"ear-foot-{side}", f(foot), (f((7, 40)), f((11, 39)), f(corner)))
            self.add_bezier(f"jowl-{side}", mouth_end, (f((22, 36)), f((17, 37)), f(corner)))
            self.relate("connect", "outline", f"ear-inner-{side}")
            self.relate("connect", "outline", f"ear-foot-{side}")
            self.relate("connect", f"ear-inner-{side}", f"ear-foot-{side}")
            self.relate("connect", f"ear-inner-{side}", f"jowl-{side}")
            self.relate("connect", f"ear-foot-{side}", f"jowl-{side}")
            self.relate("connect", "mouth", f"jowl-{side}")
        self.relate("connect", "jowl-l", "jowl-r")
