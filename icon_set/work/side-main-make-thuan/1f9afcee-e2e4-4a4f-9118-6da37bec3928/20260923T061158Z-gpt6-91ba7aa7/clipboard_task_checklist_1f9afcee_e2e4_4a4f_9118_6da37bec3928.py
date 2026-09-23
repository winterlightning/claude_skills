"""A clipped task board with two list rows."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1f9afcee-e2e4-4a4f-9118-6da37bec3928"
SOURCE_PATH = "pictographic-primitives/office/task list text 1_1f9afcee-e2e4-4a4f-9118-6da37bec3928.svg"
AUTHOR = "gpt-6"


class ClipboardTaskChecklist(Solo48):
    icon_id = "clipboard-task-checklist"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/stationery"
    aliases = ("task clipboard", "list board")
    keywords = ("tasks", "checklist", "notes", "clipboard")

    def build(self) -> None:
        # The semicircular clip rises above the board's top edge. Two rows
        # repeat a compact marker and a text line on the same baselines.
        self.add_line("top-left", (12, 8), (19, 8))
        self.add_line("clip-base", (19, 8), (29, 8))
        self.add_line("top-right", (29, 8), (36, 8))
        self.add_arc("ne", (36, 8), (40, 12), radius_x=4)
        self.add_line("right", (40, 12), (40, 40))
        self.add_arc("se", (40, 40), (36, 44), radius_x=4)
        self.add_line("bottom", (36, 44), (12, 44))
        self.add_arc("sw", (12, 44), (8, 40), radius_x=4)
        self.add_line("left", (8, 40), (8, 12))
        self.add_arc("nw", (8, 12), (12, 8), radius_x=4)
        self.add_contour("board", "top-left", "clip-base", "top-right",
                         "ne", "right", "se", "bottom", "sw", "left",
                         "nw", closed=True)
        self.add_arc("clip-arch", (19, 8), (29, 8),
                     radius_x=5, radius_y=4, sweep=True)
        self.relate("connect", "clip-arch", "clip-base")
        for index, y in enumerate((19, 33)):
            self.add_dot(f"task-marker-{index}", (18, y))
            self.add_line(f"task-text-{index}", (27, y), (31, y))
