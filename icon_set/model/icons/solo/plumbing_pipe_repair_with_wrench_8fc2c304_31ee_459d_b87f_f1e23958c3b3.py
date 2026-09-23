from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "8fc2c304-31ee-459d-b87f-f1e23958c3b3"
SOURCE_PATH = "pictographic-primitives/_uncategorized_22/home improvement 14_8fc2c304-31ee-459d-b87f-f1e23958c3b3.svg"
AUTHOR = "gpt-6"

class PlumbingPipeRepairWithWrench(Solo48):
    icon_id = "plumbing-pipe-repair-with-wrench"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/plumbing"
    aliases = ("pipe leak repair",)
    keywords = ("elbow pipe", "water drop", "wrench")

    def build(self) -> None:
        # Pipe spans the upper row; droplet and diagonal wrench occupy lower corners.
        self.add_polyline("elbow-pipe", (44, 12), (18, 12), (18, 8), (8, 8), (4, 12), (4, 16), (8, 20), (44, 20))
        self.add_polyline("droplet", (10, 28), (16, 36), (14, 40), (6, 40), (4, 36), (10, 28), closed=True)
        self.add_polyline("wrench-jaw", (24, 28), (24, 34), (28, 36), (32, 34), (34, 30))
        self.add_line("wrench-handle", (32, 34), (44, 40))
        self.relate("connect", "wrench-jaw", "wrench-handle")
