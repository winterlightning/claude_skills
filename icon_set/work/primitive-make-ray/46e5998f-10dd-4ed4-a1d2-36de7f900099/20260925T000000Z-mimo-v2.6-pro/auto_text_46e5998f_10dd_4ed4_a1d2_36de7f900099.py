"""AUTO wordmark, hand-authored as one SOLO48 text icon.

Plan: a compact two-row AUTO wordmark on the VRECT_M envelope, preserving every letter and the A-U-T-O reading order. The rows use shared integer baselines and deliberate letter-count rhythm. The source is reconstructed as readable letterforms rather than trace coordinates. Lucide construction reference: local monoline typeface glyphs where available; no equivalent match was required because the supplied text itself is the subject.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "46e5998f-10dd-4ed4-a1d2-36de7f900099"
SOURCE_PATH = "icon_set/work/todo-references/auto (text)_46e5998f-10dd-4ed4-a1d2-36de7f900099.svg"
AUTHOR = "mimo-v2.6-pro"


class AutoText(Solo48):
    icon_id = "auto-text"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "typeface"
    aliases = ("auto", "automatic")
    keywords = ("auto", "text", "wordmark", "typography")

    def build(self) -> None:
        # VRECT_M centerline box (10,4)-(38,44). Rows are A-U / T-O.
        self.add_line("a-left", (10, 18), (15, 4))
        self.add_line("a-right", (15, 4), (20, 18))
        self.add_line("a-cross", (20, 18), (10, 18))
        self.add_contour("a", "a-left", "a-right", "a-cross", closed=True)

        self.add_line("u-left", (28, 4), (28, 16))
        self.add_line("u-bottom", (28, 16), (38, 16))
        self.add_line("u-right", (38, 16), (38, 4))
        self.add_contour("u", "u-left", "u-bowl", "u-right", closed=False)

        self.add_line("t-bar", (10, 28), (20, 28))
        self.add_line("t-stem", (15, 28), (15, 44))
        self.relate("connect", "t-bar", "t-stem")

        self.add_arc("o-top-left", (28, 34), (33, 32), radius_x=5, radius_y=2, sweep=True)
        self.add_arc("o-top-right", (33, 32), (38, 34), radius_x=5, radius_y=2, sweep=True)
        self.add_line("o-right", (38, 34), (38, 42))
        self.add_arc("o-bottom-right", (38, 42), (33, 44), radius_x=5, radius_y=2, sweep=True)
        self.add_arc("o-bottom-left", (33, 44), (28, 42), radius_x=5, radius_y=2, sweep=True)
        self.add_line("o-left", (28, 42), (28, 34))
        self.add_contour("o", "o-top-left", "o-top-right", "o-right", "o-bottom-right", "o-bottom-left", "o-left", closed=True)
