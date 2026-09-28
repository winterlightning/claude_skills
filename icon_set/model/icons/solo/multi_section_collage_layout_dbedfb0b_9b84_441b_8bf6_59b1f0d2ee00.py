"""A rounded collage canvas partitioned into five unequal panels.

SQUARE extrema (6,6)-(42,42). Shared divider nodes own the stepped panel
scheme. Lucide layout-dashboard informed panel grouping; source owns ratios.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "dbedfb0b-9b84-441b-8bf6-59b1f0d2ee00"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/composition layout 1_dbedfb0b-9b84-441b-8bf6-59b1f0d2ee00.svg"
AUTHOR = "gpt-6"


class MultiSectionCollageLayout(Solo48):
    icon_id = "multi-section-collage-layout"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("collage grid", "composition layout")
    keywords = ("panels", "mosaic", "sections", "grid")

    def build(self) -> None:
        p = [(9,6),(28,6),(39,6),(42,9),(42,18),(42,28),(42,39),(39,42),(28,42),(18,42),(9,42),(6,39),(6,28),(6,9),(9,6)]
        members=[]
        arc_indices={2,6,10,13}
        for i,(a,b) in enumerate(zip(p,p[1:])):
            name=f"frame-{i}"
            if i in arc_indices:
                self.add_arc(name,a,b,radius_x=3,radius_y=3,sweep=True)
            else:
                self.add_line(name,a,b)
            members.append(name)
        self.add_contour("frame", *members, closed=True)
        self.add_line("main-vertical", (28,6), (28,42))
        self.add_line("main-horizontal", (6,28), (42,28))
        self.add_line("upper-right-split", (28,18), (42,18))
        self.add_line("lower-left-split", (18,28), (18,42))
        for name in ("main-vertical", "main-horizontal", "upper-right-split", "lower-left-split"):
            self.relate("connect", name, "frame")
        for a,b in (("main-vertical","main-horizontal"),("main-vertical","upper-right-split"),("main-horizontal","lower-left-split")):
            self.relate("connect",a,b)
