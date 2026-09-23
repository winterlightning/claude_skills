from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "dde7dc1d-8399-4ae0-b88b-2f4982119ff4"
SOURCE_PATH = "pictographic-primitives/_uncategorized_22/home improvement 6_dde7dc1d-8399-4ae0-b88b-2f4982119ff4.svg"
AUTHOR = "gpt-6"

class FenceAndToolBox(Solo48):
    icon_id = "fence-and-tool-box"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/home-improvement"
    aliases = ("fence toolbox",)
    keywords = ("pickets", "tools", "case")

    def build(self) -> None:
        # Repeated pointed pickets above a handled toolbox; one rail joins the posts.
        for name, left in (("left", 4), ("middle", 20), ("right", 36)):
            self.add_polyline(name + "-picket", (left, 16), (left, 12), (left + 4, 8), (left + 8, 12), (left + 8, 16))
        for name, a, b, p, q in (("rail-left", (12, 16), (20, 16), "left-picket", "middle-picket"), ("rail-right", (28, 16), (36, 16), "middle-picket", "right-picket")):
            self.add_line(name, a, b)
            self.relate("connect", name, p)
            self.relate("connect", name, q)
        self.add_polyline("toolbox", (12, 32), (36, 32), (36, 40), (12, 40), (12, 32), closed=True)
        self.add_polyline("handle", (20, 32), (20, 24), (28, 24), (28, 32))
        self.relate("connect", "toolbox", "handle")
