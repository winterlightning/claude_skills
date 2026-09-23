"""A wide empty image placeholder above three text strokes.

Symbol plan: one rectangular frame and a three-member line series with shared
left alignment and 8-unit row pitch. SQUARE bounds x/y 6..42.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "18a36e5c-54bf-4249-88cb-6a0d5c4282b3"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/insert image top_18a36e5c-54bf-4249-88cb-6a0d5c4282b3.svg"
AUTHOR = "gpt-6"


class ImageOnTopOfText(Solo48):
    icon_id = "image-on-top-of-text"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/layout"
    aliases = ("insert image top", "image above text")
    keywords = ("image", "placeholder", "text", "layout", "top")

    def build(self) -> None:
        self.add_polyline("image-frame", (6, 6), (42, 6), (42, 18), (6, 18), closed=True)
        for index, (y, x_end) in enumerate(((26, 34), (34, 42), (42, 34)), 1):
            self.add_line(f"content-line-{index}", (6, y), (x_end, y))
