"""Happy person bust with circular head, raised shoulders, and enclosing circle."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import circle

SOURCE_ICON_ID = "a8d49b9d-bc09-4bb6-a4b0-570e012f07c0"
SOURCE_PATH = "pictographic-primitives/other/person_a8d49b9d-bc09-4bb6-a4b0-570e012f07c0.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "happy-person-in-a-circle"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/person"
    aliases = ("happy-user-circle",)
    keywords = ("person", "user", "happy", "circle")

    def build(self):
        circle(self, "frame", 16, 16, 14)
        circle(self, "head", 16, 10, 4)
        self.add_bezier("shoulder-left", (8, 19), ((10, 22), (13, 22), (16, 22)))
        self.add_bezier("shoulder-right", (16, 22), ((19, 22), (22, 22), (24, 19)))
        self.add_contour("shoulders", "shoulder-left", "shoulder-right")
        self.add_line("torso", (16, 22), (16, 27))
        self.relate("connect", "shoulders", "torso")
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
