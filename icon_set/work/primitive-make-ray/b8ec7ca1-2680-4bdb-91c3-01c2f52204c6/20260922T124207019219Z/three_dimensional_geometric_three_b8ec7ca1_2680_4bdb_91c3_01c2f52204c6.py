"""Folded geometric numeral three.

Plan: SQUARE centerline extremes (6,6)-(42,42); angular folded ribbon,
upper/lower trapezoidal faces and a central diamond share explicit vertices.
The source supplies the complete face layout; Lucide box supplies the principle
of a sparse face network with shared junctions. Perspective remains asymmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b8ec7ca1-2680-4bdb-91c3-01c2f52204c6"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/3ds max logo_b8ec7ca1-2680-4bdb-91c3-01c2f52204c6.svg"
AUTHOR = "gpt-6"

class ThreeDimensionalGeometricThree(Solo48):
    icon_id = "three-dimensional-geometric-three"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/numerals"
    aliases = ("3ds max logo", "folded three")
    keywords = ("three", "3", "geometric", "3d", "folded", "logo")

    def build(self):
        nodes = {
            "top-left": (10,6), "top-right": (30,6),
            "upper-left": (6,14), "upper-fold": (24,14),
            "apex": (42,26), "lower-right": (30,42),
            "bottom-left": (10,42), "lower-left": (6,34),
            "lower-fold": (30,34), "diamond-top": (15,17),
            "diamond-left": (8,24), "diamond-bottom": (15,32),
            "center-top": (24,20), "center-bottom": (24,30),
        }
        perimeter = ["top-left", "top-right", "apex", "lower-right",
                     "bottom-left", "lower-left", "diamond-bottom",
                     "diamond-left", "diamond-top", "upper-left", "top-left"]
        edges = []
        for i,(a,b) in enumerate(zip(perimeter,perimeter[1:])):
            edges.append((f"outline-{i}",a,b))
        for name,a,b in [
            ("top-face", "upper-left", "upper-fold"),
            ("top-depth", "upper-fold", "top-right"),
            ("upper-diagonal", "upper-fold", "apex"),
            ("upper-inner-left", "diamond-top", "center-top"),
            ("upper-inner-right", "center-top", "apex"),
            ("lower-inner-left", "diamond-bottom", "center-bottom"),
            ("lower-inner-right", "center-bottom", "apex"),
            ("center-depth", "center-top", "center-bottom"),
            ("bottom-face", "lower-left", "lower-fold"),
            ("bottom-depth", "lower-fold", "lower-right"),
            ("lower-diagonal", "lower-fold", "apex"),
        ]:
            edges.append((name,a,b))
        for name,a,b in edges:
            self.add_line(name,nodes[a],nodes[b])
        self.add_contour("outline",*(f"outline-{i}" for i in range(len(perimeter)-1)),closed=True)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b} & {c,d}:
                    self.relate("connect", name, other)
