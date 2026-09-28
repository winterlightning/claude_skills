"""A Bernese mountain dog face: domed head with floppy ears, two jowl lobes, nose and neck.

Symbol plan: mirrored about x=24. The head is one cubic run from the left ear tip B over
the ear's outer extreme (x=6), the domed crown (y=6) and down to the right ear tip. From
each ear tip a jowl lobe dips to its low point and rises to the central notch N, and a
neck line falls to the bottom corner. The nose is a round-capped bar with a stem to N.
Lucide construction: 'dog' - head silhouette from few cubic runs, ears as rounded lobes.
Keyshape SQUARE: centerline x 6..42 (ear extremes, neck feet), y 6..42 (crown, neck feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "abf9d7c5-9b5d-543d-86fe-9e1ff0364cb2"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__bernese-mountain-dog-face/20260926T030905Z-thuan-mac/reference/bernese mountain dog_abf9d7c5-9b5d-543d-86fe-9e1ff0364cb2.svg"
AUTHOR = "claude-opus-5-5"


class BerneseMountainDogFace(Solo48):
    icon_id = "bernese-mountain-dog-face"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ("bernese-mountain-dog", "berner")
    keywords = ("dog", "bernese", "mountain-dog", "face", "breed", "pet", "floppy-ears", "puppy")

    def build(self) -> None:
        m = lambda p: (48 - p[0], p[1])
        B, O, T = (9, 27), (6, 19), (18, 6)
        self.add_bezier("head", B,
                        ((7.5, 25), (6, 22), O),
                        ((6, 15), (13, 6), T),
                        ((21, 6), (27, 6), m(T)),
                        ((35, 6), (42, 15), m(O)),
                        ((42, 22), (40.5, 25), m(B)))
        L, N = (16, 38), (24, 33)
        self.add_bezier("jowl-left", B, ((10, 33), (12, 38), L), ((19, 38), (21, 34.5), N))
        self.add_bezier("jowl-right", m(B), ((38, 33), (36, 38), m(L)), ((29, 38), (27, 34.5), N))
        self.add_bezier("neck-left", B, ((8, 32), (6, 37), (6, 42)))
        self.add_bezier("neck-right", m(B), ((40, 32), (42, 37), (42, 42)))
        self.add_line("nose", (21, 23), (27, 23))
        self.add_line("nose-stem", (24, 23), (24, 33))
        for a, b in (("head", "jowl-left"), ("head", "jowl-right"), ("head", "neck-left"),
                     ("head", "neck-right"), ("jowl-left", "neck-left"), ("jowl-right", "neck-right"),
                     ("jowl-left", "jowl-right"), ("nose", "nose-stem"),
                     ("jowl-left", "nose-stem"), ("jowl-right", "nose-stem")):
            self.relate("connect", a, b)
