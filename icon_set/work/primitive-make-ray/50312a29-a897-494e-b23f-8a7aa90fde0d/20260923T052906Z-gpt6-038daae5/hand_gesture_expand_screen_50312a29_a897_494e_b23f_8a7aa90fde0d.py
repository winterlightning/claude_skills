from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "50312a29-a897-494e-b23f-8a7aa90fde0d"
SOURCE_PATH = "pictographic-primitives/_uncategorized_22/hand gesture control expand_50312a29-a897-494e-b23f-8a7aa90fde0d.svg"
AUTHOR = "gpt-6"

class HandGestureExpandScreen(Solo48):
    icon_id = "hand-gesture-expand-screen"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("expand screen hand",)
    keywords = ("hand", "corner arrows", "expand")

    def build(self) -> None:
        # Central pointing hand is framed by three diagonal expand arrows and the source's lower-right corner remnant.
        self.add_polyline("hand", (20, 34), (20, 26), (22, 26), (22, 18), (24, 14), (28, 14), (30, 18), (30, 24), (34, 24), (34, 30), (32, 34), (20, 34), closed=True)
        for name, points, tip in (("upper-left", ((12, 6), (6, 6), (6, 12)), (12, 12)), ("upper-right", ((36, 6), (42, 6), (42, 12)), (36, 12)), ("lower-left", ((6, 36), (6, 42), (12, 42)), (12, 36))):
            self.add_polyline(name, *points)
            self.add_line(name + "-shaft", points[1], tip)
            self.relate("connect", name, name + "-shaft")
        self.add_polyline("lower-right-corner", (42, 36), (42, 42), (38, 42))
