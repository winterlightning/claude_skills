from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "91c94c77-d58a-4060-b5b2-58ea91814e5f"
SOURCE_PATH = "pictographic-primitives/_uncategorized_19/frame_91c94c77-d58a-4060-b5b2-58ea91814e5f.svg"
AUTHOR = "gpt-6"

class RoundedSquarePictureFrame(Solo48):
    icon_id = "rounded-square-picture-frame"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("square frame", "photo frame")
    keywords = ("picture", "border", "rounded")

    def build(self) -> None:
        # Concentric rounded squares share an axis and corner radius.
        self.add_polyline("outer-frame", (10, 6), (38, 6), (42, 10), (42, 38), (38, 42), (10, 42), (6, 38), (6, 10), (10, 6), closed=True)
        self.add_polyline("inner-frame", (18, 14), (30, 14), (34, 18), (34, 30), (30, 34), (18, 34), (14, 30), (14, 18), (18, 14), closed=True)
