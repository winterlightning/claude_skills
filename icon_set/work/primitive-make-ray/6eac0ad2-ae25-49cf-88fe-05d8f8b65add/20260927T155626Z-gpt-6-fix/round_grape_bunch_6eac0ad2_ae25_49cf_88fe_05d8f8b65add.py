"""Scalloped sugar apple, preserving the original fruit cluster and short stem."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6eac0ad2-ae25-49cf-88fe-05d8f8b65add"
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-grape-bunch/20260927T155415Z-thuan-mac-1/reference/sugar apple_6eac0ad2-ae25-49cf-88fe-05d8f8b65add.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = "round-grape-bunch"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ("sugar apple", "fruit", "bunch", "berry", "stem")

    def build(self):
        # One connected scalloped rind retains the overlapping round lobes.
        pts = [
            ((20, 11), (16, 13), (14, 15)),
            ((10, 14), (8, 18), (8, 23)),
            ((9, 25), (11, 26), (13, 26)),
            ((8, 28), (8, 34), (14, 37)),
            ((14, 42), (20, 44), (24, 44)),
            ((28, 44), (34, 42), (34, 37)),
            ((40, 34), (40, 28), (35, 26)),
            ((37, 26), (39, 25), (40, 23)),
            ((40, 18), (38, 14), (34, 15)),
            ((32, 13), (28, 11), (24, 14)),
        ]
        p = (24, 14)
        ids = []
        for j, controls in enumerate(pts):
            n = f"rind-{j}"
            self.add_bezier(n, p, controls)
            ids.append(n)
            p = controls[-1]
        self.add_contour("rind", *ids, closed=True)
        self.add_line("stem", (24, 14), (27, 4))
        self.relate("connect", "rind", "stem")
        self.add_arc("centre-a", (21, 27), (27, 27), radius_x=3)
        self.add_arc("centre-b", (27, 27), (21, 27), radius_x=3)
        self.add_contour("centre-lobe", "centre-a", "centre-b", closed=True)
