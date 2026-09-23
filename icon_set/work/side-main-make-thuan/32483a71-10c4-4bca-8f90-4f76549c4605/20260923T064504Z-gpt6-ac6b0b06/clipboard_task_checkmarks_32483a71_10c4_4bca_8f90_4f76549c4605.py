"""A clipboard holding two checked tasks."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "32483a71-10c4-4bca-8f90-4f76549c4605"
SOURCE_PATH = "pictographic-primitives/interface-essential/task checklist_32483a71-10c4-4bca-8f90-4f76549c4605.svg"
AUTHOR = "gpt-6"


class ClipboardTaskCheckmarks(Solo48):
    icon_id = "clipboard-task-checkmarks"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/office"
    aliases = ("task checklist", "completed task list")
    keywords = ("clipboard", "checks", "tasks", "list")

    def build(self) -> None:
        # Board outline remains open where the centered clip attaches.
        self.add_line("board-top-left", (18, 8), (12, 8))
        self.add_arc("board-nw", (12, 8), (8, 12), radius_x=4, sweep=False)
        self.add_line("board-left", (8, 12), (8, 40))
        self.add_arc("board-sw", (8, 40), (12, 44), radius_x=4, sweep=False)
        self.add_line("board-bottom", (12, 44), (36, 44))
        self.add_arc("board-se", (36, 44), (40, 40), radius_x=4, sweep=False)
        self.add_line("board-right", (40, 40), (40, 12))
        self.add_arc("board-ne", (40, 12), (36, 8), radius_x=4, sweep=False)
        self.add_line("board-top-right", (36, 8), (30, 8))
        self.add_contour("board", "board-top-left", "board-nw", "board-left",
                         "board-sw", "board-bottom", "board-se", "board-right",
                         "board-ne", "board-top-right")

        # The short clip base merges with the board edge on this grid.
        self.add_line("clip-shoulder-left", (18, 8), (20, 8))
        self.add_arc("clip-arch", (20, 8), (28, 8), radius_x=4, sweep=True)
        self.add_line("clip-shoulder-right", (28, 8), (30, 8))
        self.add_contour("clip", "clip-shoulder-left", "clip-arch",
                         "clip-shoulder-right")
        self.relate("connect", "board-top-left", "clip-shoulder-left")
        self.relate("connect", "board-top-right", "clip-shoulder-right")

        # Two repeated check-and-rule rows, derived from one row definition.
        for index, dy in enumerate((0, 12), start=1):
            self.add_polyline(f"check-{index}", (17, 21 + dy),
                              (19, 23 + dy), (21, 19 + dy))
            self.add_line(f"rule-{index}", (29, 21 + dy), (31, 21 + dy))
