"""A blank notepad with three top binding posts."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "bff981b1-e1fa-524a-83ac-14e5d932e17b"
SOURCE_PATH = "pictographic-primitives/content/note_bff981b1-e1fa-524a-83ac-14e5d932e17b.svg"
AUTHOR = "gpt-6"


class TopBoundSpiralNotepad(Solo48):
    icon_id = "top-bound-spiral-notepad"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    categories = ("primitives", "content")
    aliases = ("notepad", "bound note")
    keywords = ("notes", "paper", "writing", "planner")

    def build(self) -> None:
        # A radius-four blank page. Splitting the top at each shared tab node
        # keeps the three-post series equal and genuinely connected.
        frame = []
        def line(name, a, b):
            self.add_line(name, a, b); frame.append(name)
        def arc(name, a, b):
            self.add_arc(name, a, b, radius_x=4); frame.append(name)
        for name, a, b in (
            ("top-0", (10, 10), (14, 10)),
            ("top-1", (14, 10), (24, 10)),
            ("top-2", (24, 10), (34, 10)),
            ("top-3", (34, 10), (38, 10)),
        ):
            line(name, a, b)
        arc("ne", (38, 10), (42, 14))
        line("right", (42, 14), (42, 38))
        arc("se", (42, 38), (38, 42))
        line("bottom", (38, 42), (10, 42))
        arc("sw", (10, 42), (6, 38))
        line("left", (6, 38), (6, 14))
        arc("nw", (6, 14), (10, 10))
        self.add_contour("page-frame", *frame, closed=True)
        for index, x in enumerate((14, 24, 34)):
            self.add_line(f"post-{index}-above", (x, 6), (x, 10))
            self.add_line(f"post-{index}-below", (x, 10), (x, 14))
            self.relate("connect", f"post-{index}-above", f"top-{index}")
            self.relate("connect", f"post-{index}-below", f"top-{index}")
