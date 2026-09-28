"""A dalmatian face: a domed head with floppy ears folded at the sides, a nose and jowls, and the neck below.

Symbol plan: symmetric about x=24. The dome arches between two branch nodes. From each
node the ear's outer edge bulges out to the envelope side and rounds under to the ear's
tip, which folds back to the face side; the face side runs from the node down past the
ear tip to the jowl corner, and the neck line continues from there to the bottom edge.
Muzzle: a small ring nose (r2, approved 4-diameter circle), a mouth line, and two jowl
curves to the jowl corners. All joins are shared endpoints.
The reference's dot eyes are dropped: dots 8 from the ears, the nose and each other do
not fit inside the face at 48.
Lucide construction: 'dog' - dome head with hanging ears and a muzzle.
Keyshape HRECT_L: centerline x 4..44 (ears), y 8..40 (dome top, neck ends).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fd0d9c0a-6ed5-48eb-b294-bbe6008deef9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dalmatian-face/20260926T044250Z-thuan-mac/reference/dalmatian_fd0d9c0a-6ed5-48eb-b294-bbe6008deef9.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    return (48 - p[0], p[1])


class DalmatianFace(Solo48):
    icon_id = "dalmatian-face"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/pets"
    aliases = ("dalmatian", "dog face", "puppy face")
    keywords = ("dog", "dalmatian", "puppy", "pet", "ears", "animal", "breed", "face")

    def build(self) -> None:
        node, apex = (11, 13), (24, 8)
        ear_tip, fold, corner, neck_end = (9, 29), (13, 26), (17, 34), (14, 40)
        self.add_bezier("dome-l", node, ((13, 9), (18, 8), apex))
        self.add_bezier("dome-r", apex, (_m((18, 8)), _m((13, 9)), _m(node)))
        self.add_contour("dome", "dome-l", "dome-r")
        nx, ny, nr = 24, 24, 2
        pts = [(nx - nr, ny), (nx, ny - nr), (nx + nr, ny), (nx, ny + nr)]
        names = ("nose-nw", "nose-ne", "nose-se", "nose-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=nr)
        self.add_contour("nose", *names, closed=True)
        mouth_end = (24, 31)
        self.add_line("mouth", (nx, ny + nr), mouth_end)
        self.relate("connect", "nose", "mouth")
        for side, f in (("l", lambda p: p), ("r", _m)):
            self.add_bezier(f"ear-{side}", f(node), (f((7, 14)), f((4, 17)), f((4, 22))),
                            (f((4, 26)), f((6, 29)), f(ear_tip)))
            self.add_line(f"ear-fold-{side}", f(ear_tip), f(fold))
            self.add_bezier(f"face-{side}", f(node), (f((12, 17)), f((13, 22)), f(fold)))
            self.add_bezier(f"cheek-{side}", f(fold), (f((13, 30)), f((15, 33)), f(corner)))
            self.add_line(f"neck-{side}", f(corner), f(neck_end))
            self.add_bezier(f"jowl-{side}", mouth_end, (f((22, 35)), f((19, 35)), f(corner)))
            for a, b in (("dome", f"ear-{side}"), ("dome", f"face-{side}"), (f"ear-{side}", f"face-{side}"),
                         (f"ear-{side}", f"ear-fold-{side}"), (f"ear-fold-{side}", f"face-{side}"),
                         (f"ear-fold-{side}", f"cheek-{side}"), (f"face-{side}", f"cheek-{side}"),
                         (f"cheek-{side}", f"neck-{side}"), (f"cheek-{side}", f"jowl-{side}"),
                         (f"neck-{side}", f"jowl-{side}"), ("mouth", f"jowl-{side}")):
                self.relate("connect", a, b)
        self.relate("connect", "jowl-l", "jowl-r")
