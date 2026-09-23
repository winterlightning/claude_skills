"""A single flagged music note inside a rounded square."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "0b1a364e-6481-4ccd-b8ea-1616ed761c6c"
SOURCE_PATH = "pictographic-primitives/other/music note square_0b1a364e-6481-4ccd-b8ea-1616ed761c6c.svg"
AUTHOR = "gpt-6"


class MusicNoteInRoundedSquare(Solo48):
    icon_id = "music-note-in-rounded-square"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ("music note square", "audio tile")
    keywords = ("song", "playlist", "music", "sound")

    def build(self) -> None:
        # A radius-four square wrapper, with a single note kept well inside.
        frame = []
        def line(name, a, b):
            self.add_line(name, a, b); frame.append(name)
        def arc(name, a, b):
            self.add_arc(name, a, b, radius_x=4); frame.append(name)
        line("top", (10, 6), (38, 6))
        arc("ne", (38, 6), (42, 10))
        line("right", (42, 10), (42, 38))
        arc("se", (42, 38), (38, 42))
        line("bottom", (38, 42), (10, 42))
        arc("sw", (10, 42), (6, 38))
        line("left", (6, 38), (6, 10))
        arc("nw", (6, 10), (10, 6))
        self.add_contour("square-frame", *frame, closed=True)

        # Head is a radius-four loop. The stem joins at its rightmost point;
        # the single curved flag matches the reference's direction.
        self.add_arc("head-lower", (24, 29), (16, 29), radius_x=4)
        self.add_arc("head-upper", (16, 29), (24, 29), radius_x=4)
        self.add_contour("notehead", "head-lower", "head-upper", closed=True)
        self.add_line("stem-lower", (24, 16), (24, 29))
        self.add_bezier("flag", (24, 16), ((30, 18), (34, 22), (30, 27)))
        self.relate("connect", "stem-lower", "head-upper")
        self.relate("connect", "flag", "stem-lower")
