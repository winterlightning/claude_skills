"""A broad speech bubble containing a check and a cross side by side.

HRECT_L extrema (4,8)-(44,40). Marks occupy mirrored left/right fields;
the cross's two strokes share its center node. Lucide message-square-check
informed the rounded message enclosure and compact check construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9e7718a2-06d5-4b71-838d-1a6badd00400"
SOURCE_PATH = "pictographic-primitives/_uncategorized_13/criteria false 1_9e7718a2-06d5-4b71-838d-1a6badd00400.svg"
AUTHOR = "gpt-6"


class SpeechBubbleWithCheckAndCross(Solo48):
    icon_id = "speech-bubble-with-check-and-cross"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/decisions"
    aliases = ("criteria true false", "yes no chat")
    keywords = ("check", "cross", "approval", "choice")

    def build(self) -> None:
        self.add_line("top",(8,8),(40,8))
        self.add_arc("ne",(40,8),(44,12),radius_x=4,radius_y=4,sweep=True)
        self.add_line("right",(44,12),(44,40))
        self.add_line("tail",(44,40),(36,34))
        self.add_line("bottom",(36,34),(8,34))
        self.add_arc("sw",(8,34),(4,30),radius_x=4,radius_y=4,sweep=True)
        self.add_line("left",(4,30),(4,12))
        self.add_arc("nw",(4,12),(8,8),radius_x=4,radius_y=4,sweep=True)
        self.add_contour("bubble","top","ne","right","tail","bottom","sw","left","nw",closed=True)
        self.add_polyline("check",(13,21),(16,25),(20,17))
        self.add_polyline("cross-a",(29,17),(32,21),(35,25))
        self.add_polyline("cross-b",(35,17),(32,21),(29,25))
        self.relate("connect","cross-a","cross-b")
